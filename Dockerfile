# Pull official base image.
FROM python:3.7-alpine


# Set work directory.
WORKDIR /home/djangoadmin/djangoapps/ana1


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install psycopg dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev



# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /home/djangoadmin/djangoapps/ana1/requirements.txt
RUN pip install -r requirements.txt


# Copy project.
COPY . /home/djangoadmin/djangoapps/ana1

