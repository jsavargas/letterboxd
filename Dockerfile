# start by pulling the python image
FROM python:3.10.2-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

#RUN apk update && apk add tzdata

# install the dependencies and packages in the requirements file
RUN pip install --upgrade pip && pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1

# copy every content from the local file to the image
COPY src /app
#COPY entry.sh /entry.sh

VOLUME /download /watch /config

EXPOSE 5000

CMD ["flask", "run"]

