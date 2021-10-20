FROM python:3
ENV PYTHONUUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django-extensions \
                django-environ \
                pandas-datareader

COPY . /code/

EXPOSE 8001
