FROM python:3.12-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

COPY requirements.txt .requirements.txt
RUN pip install -r .requirements.txt

COPY manage.py ./manage.py
COPY VAGKereso ./VAGKereso

EXPOSE 8000

FROM production as development

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .
