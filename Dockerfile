FROM python:3.10

EXPOSE 5000

COPY . /opt/services/bot

RUN mkdir -p /opt/services/bot/imran-bot
WORKDIR /opt/services/bot/imran-bot

RUN mkdir -p /opt/services/bot/imran-bot/requirements
ADD requirements.txt /opt/services/bot/imran-bot/


COPY . /opt/services/bot/imran-bot/

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bot/imran-bot/main.py"]