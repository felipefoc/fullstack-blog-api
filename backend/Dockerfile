FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint /entrypoint

RUN sed -i 's/\r$//g' /entrypoint

RUN chmod +x /entrypoint

WORKDIR /code

ENTRYPOINT ["/entrypoint"]

