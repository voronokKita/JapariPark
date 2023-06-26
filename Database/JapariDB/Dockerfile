FROM postgres:15-alpine3.18

LABEL author="github.com/voronokKita"
LABEL description="Japari Park main database."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=japari_data_user_pass,env=MYSECRET`"
LABEL logs="Mount /JapariData/logs to get them."


# < as root >
# < working with the environment >
EXPOSE 5432/tcp
ENV POSTGRES_PORT=5432
ENV BASE_DIR=/JapariData
ENV LOGS_DIR=/JapariData/logs
ENV CONFIGS_DIR=/JapariData/configs

ENV PGDATA=/var/lib/postgresql/data/pgdata
ENV POSTGRES_USER=luckybot
ENV POSTGRES_DB=japari_park_database


# Add some tools and sudo
RUN apk update \
    && apk add --no-cache \
        sudo \
        curl \
        vim \
    && echo "%wheel ALL=(ALL) ALL" | EDITOR='tee -a' visudo \
    && echo "$POSTGRES_USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo


# Make the base dir;
# make dirs for the logs, secrets and configs:
WORKDIR "$BASE_DIR"
RUN chmod 777 "$BASE_DIR" \
    && mkdir --mode=776 "$BASE_DIR/logs" \
    && mkdir --mode=774 "$BASE_DIR/secrets" \
    && mkdir --mode=774 "$BASE_DIR/configs"

COPY --chmod=776 Dockerfile docker-compose.yaml ./
COPY --chmod=777 ./tests ./tests
