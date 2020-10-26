all: build run


run: build
	docker run -it -p 16000:80 martinenders/mini-web-apps
build:
	docker build -t martinenders/mini-web-apps:latest .
push: build
	docker push martinenders/mini-web-apps:latest
