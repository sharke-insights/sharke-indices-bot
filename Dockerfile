FROM python:3.7

ENV TZ America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /bot

ADD requirements.txt /bot

RUN pip install -r requirements.txt

ADD . /bot

CMD python run.py
