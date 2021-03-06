FROM python:3.8-alpine

RUN mkdir -p /usr/src/
WORKDIR /usr/src/

COPY requirements.txt /usr/src/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src/app.py /usr/src/

WORKDIR /usr/src/

ENTRYPOINT ["python"]
CMD ["app.py"]