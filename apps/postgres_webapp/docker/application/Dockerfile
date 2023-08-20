FROM python:3.6

WORKDIR /postgres_webapp/

COPY ./application/ ./application/
COPY ./manage.py .
COPY ./requirements.txt .

RUN apt update
RUN apt install -y vim
RUN apt install -y iputils-ping net-tools 
RUN pip install --upgrade pip
RUN pip install django
RUN pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
