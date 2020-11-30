FROM python:3-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app 

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "main.py" ]
