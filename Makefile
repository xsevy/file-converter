.DEFAULT_GOAL:=help

help:
	@echo "\nUsage:\n  make \033[32m<target>\033[0m\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\t\033[32m%-30s\033[0m %s\n", $$1, $$2}'

build:  ## Build the app
	@docker compose build

convert:  ## Convert file. Requires INPUT_PATH and OUTPUT_PATH positional arguments.
	@docker compose run --rm converter python main.py --input-path ${INPUT_PATH} --output-path ${OUTPUT_PATH}
