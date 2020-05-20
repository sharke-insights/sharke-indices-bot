FROM python:3.7

WORKDIR /bot

ADD requirements.txt /bot

RUN pip install -r requirements.txt

ADD . /bot

CMD python run.py
