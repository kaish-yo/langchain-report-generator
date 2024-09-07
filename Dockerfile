FROM python:3.12.5-slim-bullseye

RUN apt-get clean && apt-get update && \
    apt-get install --no-install-recommends -y \
    git \
    gcc \
    curl \
    vim \
    wget \
    graphviz-dev

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# change workind directory before copying source files
WORKDIR /usr/src

# copy source files
COPY . .

# install dependencies
RUN poetry install --no-root

# CMD fastapi dev app/main.py