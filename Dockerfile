FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install flask==0.12.2
EXPOSE 8080

ENTRYPOINT ['python3']
CMD ['black_jack.py']