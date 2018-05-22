DOCKER=docker
IMAGE_NAME=ai
build:
	$(DOCKER) build -t $(IMAGE_NAME) . 

run:
	$(DOCKER) run \
        -p 4000:80 \
        $(IMAGE_NAME) \
        

clean:
	rm -rf volume/

clear: clean

all: build run
