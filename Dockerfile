FROM python:3.6

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code/

CMD ["inv", "server.start"]
EXPOSE 5000/tcp
