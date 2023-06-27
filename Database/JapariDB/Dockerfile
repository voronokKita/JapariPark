FROM postgres:15-alpine3.18

LABEL author="github.com/voronokKita"
LABEL description="Japari Park mono database."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=japari_data_user_pass,env=MYSECRET`"
LABEL logs="Mount /JapariData/logs to get them."


# << as root >>
# <Environment setup>
EXPOSE 5432/tcp
ENV POSTGRES_PORT=5432
ENV BASE_DIR=/JapariData
ENV LOGS_DIR=/JapariData/logs
ENV CONFIGS_DIR=/JapariData/configs

ENV TOP_USER=postgres
ENV BASE_GROUP=postgres
ENV USER=luckybot
ENV UID=1000
ENV GID=70

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
    && echo "%postgres ALL=(ALL) ALL" | EDITOR='tee -a' visudo


# <User setup>
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

# Add to the administrators group and to the sudoers
RUN addgroup $USER wheel \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo
# </User setup>
# </Environment setup>


# <Files setup>
# Resolve the PGDATA and the Postgres vars directories
RUN mkdir -p /var/lib/postgresql/data \
    && chown "$UID:$GID" /var/lib/postgresql/data \
    && chmod 775 /var/lib/postgresql/data \
    \
    && mkdir -p /var/run/postgresql \
    && chown "$UID:$GID" /var/run/postgresql \
    && chmod 775 /var/run/postgresql

# Make the base dir and dir for the logs
RUN mkdir --mode=775 "$BASE_DIR" \
    && mkdir --mode=775 "$BASE_DIR/logs" \
    && chown "$UID:$GID" "$BASE_DIR" \
    && chown "$UID:$GID" "$BASE_DIR/logs"

COPY --chown="$UID:$GID" --chmod=555 Dockerfile docker-compose.yaml requirements.txt ./
COPY --chown="$UID:$GID" --chmod=555 ./tests ./tests
# </Files setup>


# << as the user >>
USER $USER
WORKDIR "$BASE_DIR"
