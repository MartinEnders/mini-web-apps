all: build run

run:
	docker run -it -p 16000:80 martinenders/mini-web-apps
build:
	docker build -t martinenders/mini-web-apps:latest .
push:
	docker push martinenders/mini-web-aps:latest
