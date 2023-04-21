.PHONY: build-env

build-env:
	micromamba create -f environment.yaml -y
