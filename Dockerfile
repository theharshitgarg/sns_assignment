FROM python:3.12.0a5-alpine3.16

WORKDIR /app
COPY . /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8000

RUN python backend/manage.py migrate
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]