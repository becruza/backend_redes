FROM python:3

MAINTAINER Becruza "becruza@unal.edu.co"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN mkdir /app/phrases

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]