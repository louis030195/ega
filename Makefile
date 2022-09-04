GCLOUD_PROJECT := $(shell gcloud config list --format 'value(core.project)' 2>/dev/null)
REGION := europe-west1
OURARING_TOKEN := $(shell cat .env | grep -w OURARING_TOKEN | cut -d "=" -f 2)
TIMINGAPP_TOKEN := $(shell cat .env | grep -w TIMINGAPP_TOKEN | cut -d "=" -f 2)
WANDB_TOKEN := $(shell cat .env | grep -w WANDB_TOKEN | cut -d "=" -f 2)

# Warn the user if no .env is found here
# using makefile syntax
ifeq (, $(shell ls .env))
$(error "No .env file found. Please create one with the appropriate variables.")
endif


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

.PHONY: help

help: # Run `make help` to get help on the make commands
	@grep -E '^[0-9a-zA-Z\/_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'