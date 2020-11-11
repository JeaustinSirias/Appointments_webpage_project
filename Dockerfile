FROM python:3.7-alpine

#Setup the python unbuffered enviroment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Copy the dependences to the docker img & install them
RUN mkdir /proyecto
WORKDIR /proyecto
RUN pip install --upgrade pip
COPY requirements.txt /proyecto/
RUN pip install -r requirements.txt
COPY . /proyecto/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
