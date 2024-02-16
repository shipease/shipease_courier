FROM python:3.10
WORKDIR  /app
COPY . .
RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations && python3 manage.py migrate
EXPOSE 8082
CMD python manage.py runserver 0.0.0.0:8082
