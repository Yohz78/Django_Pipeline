# syntax=docker/dockerfile:1
# Pull the image
FROM python:3.8-slim-buster

#  Working directoy
WORKDIR /app

# create a user
RUN addgroup --system django \
    && adduser --system --ingroup django django

# Set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

RUN python manage.py collectstatic --noinput --clear

USER django

CMD web gunicorn oc_lettings_site.wsgi:application