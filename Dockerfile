FROM python:3.9.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED 1

# Install Python Dependencies
COPY ./requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN useradd hierarchy && chown -R hierarchy /app
USER hierarchy

CMD ["python", "-m", "hierarchy",  "-r", "Input/roles.json", "-u", "Input/users.json"]