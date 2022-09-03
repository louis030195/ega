
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

.PHONY: help

help: # Run `make help` to get help on the make commands
	@grep -E '^[0-9a-zA-Z\/_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'