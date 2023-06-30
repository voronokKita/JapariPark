FROM postgres:15-alpine3.18

LABEL name="JapariDB"
LABEL description="Japari Park mono database."
LABEL author="github.com/voronokKita"
LABEL logs="Mount /JapariDB/logs to get them."
LABEL building_secret="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=japari_data_build_pass,env=MYSECRET`"


# << as root >>
# <Environment setup>
EXPOSE 5432
ENV POSTGRES_PORT=5432
ENV BASE_DIR=/JapariDB
ENV LOGS_DIR=/JapariDB/logs
ENV CONFIGS_DIR=/JapariDB/configs

ENV BASE_USER=postgres
ENV BASE_GROUP=postgres
ENV GID=70
ENV USER=luckybot
ENV UID=1000

# <Configs>
ENV PGDATA=/var/lib/postgresql/data/pgdata
ENV POSTGRES_USER=honeybot
ENV POSTGRES_DB=japari_park_default
# </Configs>


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
RUN --mount=type=secret,id=japari_data_build_pass,target=/run/secrets/user_pass,required=true \
    echo "$USER:$(cat /run/secrets/user_pass)" | chpasswd

# Add to the administrators group and to the sudoers
RUN addgroup $USER wheel \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo
# </User setup>
# </Environment setup>


# <Files setup>
# Resolve the PGDATA, configs and the Postgres vars directories
RUN mkdir -p /var/lib/postgresql/data \
    && chown "$UID:$GID" /var/lib/postgresql/data \
    && chmod 775 /var/lib/postgresql/data \
    \
    && mkdir -p /var/run/postgresql \
    && chown "$UID:$GID" /var/run/postgresql \
    && chmod 775 /var/run/postgresql

# Make the base dir and dirs for the logs and configs
RUN mkdir --mode=775 $BASE_DIR \
    && mkdir --mode=775 $LOGS_DIR \
    && mkdir --mode=775 $CONFIGS_DIR \
    && chown "$UID:$GID" $BASE_DIR $LOGS_DIR $CONFIGS_DIR

COPY --chown="$UID:$GID" --chmod=555 Dockerfile docker-compose.yaml requirements.txt ./
COPY --chown="$UID:$GID" --chmod=555 ./initdb /docker-entrypoint-initdb.d
# </Files setup>


# << as the user >>
USER $USER
WORKDIR $BASE_DIR
