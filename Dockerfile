FROM python:3.10

RUN mkdir /Mango_Read_API

WORKDIR /Mango_Read_API/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /Mango_Read_API

CMD ["python","manage.py","runserver","0.0.0.8000"]