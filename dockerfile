FROM python:3.9

WORKDIR /may

ENV FLASK_APP=may.py


COPY . .

RUN pip install -r requirements.txt

EXPOSE 5002

CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
