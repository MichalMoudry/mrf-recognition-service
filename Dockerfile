FROM python:3.11.5-slim as build

# Configure poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR="/opt/.cache"

# Install poetry
RUN python3 -m venv $POETRY_HOME \
    && $POETRY_HOME/bin/pip install -U pip setuptools \
    && $POETRY_HOME/bin/pip install poetry==1.6.0

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root --no-ansi --without dev

FROM python:3.11.5-slim as release
WORKDIR /app

#ENV PYTHONDONTWRITEBYTECODE=1 \
#    PYTHONUNBUFFERED=1 \
#    PATH="/app/.venv/bin:$PATH"
ENV PATH="/app/.venv/bin:$PATH"

COPY --from=build /app/.venv/ ./.venv

RUN apt-get update \
    && apt-get -y install tesseract-ocr