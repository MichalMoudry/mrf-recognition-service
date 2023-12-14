FROM python:3.12.1 as build
ARG ENVIRONMENT

# Configure poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR="/opt/.cache"

# Install poetry
RUN python3 -m venv $POETRY_HOME \
    && $POETRY_HOME/bin/pip install -U pip setuptools \
    && $POETRY_HOME/bin/pip install poetry==1.7.1

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app
COPY . .

RUN poetry install --no-root --no-ansi --without test

# -------------- Release section --------------
FROM python:3.12.1-alpine3.19 as release
ARG ENVIRONMENT
WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY --from=build /app/.venv/ ./.venv
COPY --from=build ./app .

EXPOSE 8000
#CMD [ "uvicorn", "app:app" ]
ENTRYPOINT ["tail", "-f", "/dev/null"]