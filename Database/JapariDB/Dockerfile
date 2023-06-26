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

ENV BASE_USER=postgres
ENV BASE_GROUP=postgres
ENV USER=luckybot
ENV UID=1000

ENV PGDATA=/var/lib/postgresql/data/pgdata
ENV POSTGRES_USER=luckybot
ENV POSTGRES_DB=japari_park_database


# Add some tools and sudo
RUN apk update \
    && apk add --no-cache \
        curl \
        vim \
        sudo \
    && echo "%wheel ALL=(ALL) ALL" | EDITOR='tee -a' visudo \
    && echo "%BASE_GROUP ALL=(ALL) ALL" | EDITOR='tee -a' visudo

# Set up a new user
RUN adduser \
      --disabled-password \
      --no-create-home \
      --gecos "" \
      --ingroup $BASE_GROUP \
      --uid $UID \
      $USER

# Setup user's password, requires BuildX or BuildKit
RUN --mount=type=secret,id=japari_data_user_pass,target=/run/secrets/user_pass,required=true \
    echo "$USER:$(cat /run/secrets/user_pass)" | chpasswd

# Add to the administrators group;
# add user to sudoers;
# resolve the PGDATA dir;
# resolve the Postgres var dir:
RUN addgroup $USER wheel \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo \
    \
    && mkdir -p /var/lib/postgresql/data \
    && chown "$USER:$BASE_GROUP" /var/lib/postgresql/data \
    && chmod 774 /var/lib/postgresql/data \
    \
    && mkdir -p /var/run/postgresql \
    && chown "$USER:$BASE_GROUP" /var/run/postgresql \
    && chmod 775 /var/run/postgresql


# Make the base dir;
# make dirs for the logs, secrets and configs:
WORKDIR "$BASE_DIR"
RUN mkdir --mode=664 "$BASE_DIR/logs" \
    && mkdir --mode=444 "$BASE_DIR/configs" \
    && chown "$USER:$BASE_GROUP" "$BASE_DIR/logs" \
    && chown "$USER:$BASE_GROUP" "$BASE_DIR/configs"

COPY --chmod=444 Dockerfile docker-compose.yaml ./
COPY --chmod=555 ./tests ./tests


USER $USER
