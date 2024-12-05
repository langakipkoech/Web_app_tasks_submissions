# official python runtime as image

FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory
WORKDIR /app

#Install dependencies
RUN pip install --upgrade pip


# copy requirements.txt to the app
COPY requirements.txt /app/

RUN pip install -r requirements.txt

# copy django project files to app
COPY . /app/

# listen on port 8000
EXPOSE 8000

# run the django project
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

