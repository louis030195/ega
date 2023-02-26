GCLOUD_PROJECT := $(shell gcloud config list --format 'value(core.project)' 2>/dev/null)
REGION := europe-west1
OURARING_TOKEN := $(shell cat .env | grep -w OURARING_TOKEN | cut -d "=" -f 2)
TIMINGAPP_TOKEN := $(shell cat .env | grep -w TIMINGAPP_TOKEN | cut -d "=" -f 2)
WANDB_TOKEN := $(shell cat .env | grep -w WANDB_TOKEN | cut -d "=" -f 2)
LASTFM_API_KEY := $(shell cat .env | grep -w LASTFM_API_KEY | cut -d "=" -f 2)
LASTFM_API_SECRET := $(shell cat .env | grep -w LASTFM_API_SECRET | cut -d "=" -f 2)
LASTFM_USERNAME := $(shell cat .env | grep -w LASTFM_USERNAME | cut -d "=" -f 2)
LASTFM_PASSWORD := $(shell cat .env | grep -w LASTFM_PASSWORD | cut -d "=" -f 2)
# get rid of '' in the string
YOUTUBE_MUSIC_HEADERS := $(shell cat .env | grep -w YOUTUBE_MUSIC_HEADERS | cut -d "=" -f 2- | sed "s/'//g")

# Warn the user if no .env is found here
# using makefile syntax
ifeq (, $(shell ls .env))
$(error "No .env file found. Please create one with the appropriate variables.")
endif

install:
	virtualenv env; \
	. env/bin/activate; \
	pip install -r requirements.txt; \
	pip install -r requirements-test.txt


push:
	git add .
	git commit -m "🙈 $(shell date +%Y-%m-%d_%H:%M:%S) 🙈"
	git push -f

deps:
	@which gcloud >/dev/null || { echo "gcloud not found in PATH"; exit 1; }
# @which firebase >/dev/null || { echo "firebase not found in PATH"; exit 1; }
	@which python3 >/dev/null || { echo "python3 not found in PATH"; exit 1; }
	@which pip3 >/dev/null || { echo "pip3 not found in PATH"; exit 1; }

codegen: ## [LOCAL DEVELOPMENT] Generate clients from openapi configurations
	rm -rf tmp_ouraring ouraring tmp_timingapp timingapp
	mkdir -p tmp_ouraring ouraring tmp_timingapp timingapp
	npx @openapitools/openapi-generator-cli generate \
		-i https://cloud.ouraring.com/v2/static/json/openapi.json \
		-g python -o ./tmp_ouraring \
		--additional-properties=generateSourceCodeOnly=true \
		--additional-properties=packageName=ouraring
	mv ./tmp_ouraring/ouraring/* ./ouraring
	npx @openapitools/openapi-generator-cli generate \
		-i https://web.timingapp.com/docs/openapi.yaml \
		-g python -o ./tmp_timingapp \
		--additional-properties=generateSourceCodeOnly=true \
		--additional-properties=packageName=timingapp
	mv ./tmp_timingapp/timingapp/* ./timingapp
	rm -rf tmp_ouraring tmp_timingapp openapitools.json



fn/experiment/start:
	gcloud scheduler jobs create pubsub ega_experiment \
		--schedule "every 24 hours" \
		--topic ega_experiment \
		--message-body $$EXPERIMENT_NAME

fn/experiment/stop:
	gcloud scheduler jobs delete ega_experiment
# TODO: complete the wandb experiment here

fn/experiment/deploy: deps ## [Local development] Deploy the function.
	gcloud beta functions deploy ega_experiment \
		--runtime python39 \
		--timeout 540 \
		--trigger-event google.pubsub.topic.publish \
		--trigger-resource ega_experiment \
		--set-env-vars OURARING_TOKEN=${OURARING_TOKEN},TIMINGAPP_TOKEN=${TIMINGAPP_TOKEN},WANDB_TOKEN=${WANDB_TOKEN} \
		--region ${REGION} \
		--memory 1024MB \
		--source functions/experiment

fn/public/deploy: deps ## [Local development] Deploy the "public" function.
# TODO: custom domain name
# firebase use ${GCLOUD_PROJECT}
# firebase deploy --only hosting
	gcloud functions deploy ega_public \
		--runtime python39 \
		--trigger-http \
		--allow-unauthenticated \
		--project ${GCLOUD_PROJECT} \
		--timeout 540s \
		--set-env-vars OURARING_TOKEN=${OURARING_TOKEN} \
		--source ./functions/public \
		--region ${REGION} \
		--memory 1024MB

# At 23:50

fn/youtube_music_to_lastfm/setup:
	gcloud pubsub topics create youtube_music_to_lastfm
	gcloud scheduler jobs create pubsub youtube_music_to_lastfm \
		--schedule "50 23 * * *" \ 
		--topic youtube_music_to_lastfm \
		--location ${REGION} \
		--message-body "youtube_music_to_lastfm"

fn/youtube_music_to_lastfm/deploy:
# write YOUTUBE_MUSIC_HEADERS to functions/youtube_music_to_lastfm/headers.json
# echo ${YOUTUBE_MUSIC_HEADERS} > functions/youtube_music_to_lastfm/headers.json
# cat .env | grep -w YOUTUBE_MUSIC_HEADERS | cut -d "=" -f 2- | sed "s/'//g" > functions/youtube_music_to_lastfm/headers.json

	gcloud functions deploy youtubee \
		--runtime python310 \
		--project ${GCLOUD_PROJECT} \
		--trigger-topic=youtube_music_to_lastfm \
		--region ${REGION} \
		--source=functions/youtube_music_to_lastfm \
		--set-env-vars LASTFM_API_KEY=${LASTFM_API_KEY},LASTFM_API_SECRET=${LASTFM_API_SECRET},LASTFM_USERNAME=${LASTFM_USERNAME},LASTFM_PASSWORD=${LASTFM_PASSWORD} \
		--max-instances 1
# rm -rf functions/youtube_music_to_lastfm/headers.json



.PHONY: help

help: # Run `make help` to get help on the make commands
	@grep -E '^[0-9a-zA-Z\/_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


# gcloud projects add-iam-policy-binding ${GCLOUD_PROJECT} --project ${GCLOUD_PROJECT} --member "serviceAccount:596120869120@cloudbuild.gserviceaccount.com" --role "roles/storage.objectViewer"
