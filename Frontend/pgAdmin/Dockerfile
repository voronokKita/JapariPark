FROM dpage/pgadmin4:7

LABEL name="pgAdmin"
LABEL description="Japari Park - pgAdmin service."
LABEL author="github.com/voronokKita"
LABEL logs="Mount /JapariPGA/logs to get them."
LABEL building_secret="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=pgadmin_user_pass,env=MYSECRET`"


# <Environment setup>
EXPOSE 80
ENV PGADMIN_PORT=80
ENV BASE_DIR=/JapariPGA
ENV LOGS_DIR=/JapariPGA/logs
ENV CONFIGS_DIR=/JapariPGA/configs

ENV PGADMIN_WORKDIR=/var/lib/pgadmin
ENV CONFIG_LOCAL=/pgadmin4/config_local.py
ENV TLS_CERT=/certs/server.cert
ENV TLS_KEY=/certs/server.key

ENV BASE_USER=pgadmin
ENV UID=5050
ENV BASE_GROUP=pgadmin
ENV GID=5050

# <Configs>
ENV PGADMIN_DEFAULT_EMAIL="admin@mail.net"
ENV PGADMIN_LISTEN_ADDRESS=0.0.0.0
ENV PGADMIN_LISTEN_PORT=80
ENV GUNICORN_THREADS=1
# </Configs>


# <root>
USER root

# Add some tools
RUN apk update && apk add --no-cache curl vim
# </Environment setup>


# <Files setup>
# Make the base dir and dirs for the logs and configs;
# backup the pgadmin workdir:
RUN mkdir --mode=775 $BASE_DIR \
    && mkdir --mode=775 $LOGS_DIR \
    && mkdir --mode=550 $CONFIGS_DIR \
    && chown "$UID:$GID" $BASE_DIR $LOGS_DIR $CONFIGS_DIR

COPY --chown="$UID:$GID" --chmod=555 Dockerfile docker-compose.yaml requirements.txt ./
# </Files setup>
# </root>


USER pgadmin
