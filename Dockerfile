FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /mango_app

WORKDIR /mango_app/

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /mango_app

CMD ["python","manage.py","runserver" ,"0.0.0.0:8000"]