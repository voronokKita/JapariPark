FROM python:3.11-alpine3.17

LABEL name="JapariService"
LABEL description="Japari Park: Service - The backend Django application with Daphne server."
LABEL author="github.com/voronokKita"
LABEL logs="Mount /JapariService/mnt-logs to get them."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=japari_service_build_pass,env=MYSECRET`"


# << as root >>
# <Environment setup>
EXPOSE 80
ENV DAPHNE_PORT=80
ENV BASE_DIR=/JapariService
ENV LOGS_DIR=/JapariService/mnt-logs
ENV LOCAL_DATA=/JapariService/mnt-data
ENV CONFIGS_DIR=/JapariService/configs

ENV GROUP=luckybot
ENV USER=luckybot
ENV GID=1000
ENV UID=1000


# Add some tools and sudo
RUN apk update \
    && apk add --no-cache \
        curl \
        coreutils \
        sudo \
    && echo "%wheel ALL=(ALL) ALL" | EDITOR='tee -a' visudo


# <User setup>
RUN addgroup $GROUP --gid $GID \
    && adduser \
        --disabled-password \
        --no-create-home \
        --gecos "" \
        --ingroup $GROUP \
        --uid $UID \
        $USER

# Setup user's password, requires BuildX or BuildKit
RUN --mount=type=secret,id=japari_service_build_pass,target=/run/secrets/user_pass,required=true \
    echo "$USER:$(cat /run/secrets/user_pass)" | chpasswd

# Add to the administrators group and to the sudoers
RUN addgroup $USER wheel \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo
# </User setup>
# </Environment setup>


# <Files setup>
# Make the base dir and dirs for the logs, configs and data
RUN mkdir --mode=775 $BASE_DIR \
    && mkdir --mode=775 $LOGS_DIR \
    && mkdir --mode=550 $CONFIGS_DIR \
    && mkdir --mode=775 $LOCAL_DATA \
    && chown "$UID:$GID" $BASE_DIR $LOGS_DIR $CONFIGS_DIR $LOCAL_DATA \
    && touch "$BASE_DIR/indocker"

# << as the user >>
USER $USER
WORKDIR $BASE_DIR

# Set up a venv and resolve the dependencies
RUN python -m venv "$BASE_DIR/venv"
ENV PATH="$BASE_DIR/venv/bin:$BASE_DIR:$PATH"
COPY --chown="$UID:$GID" --chmod=775 requirements.txt ./
RUN pip install --no-cache -r requirements.txt


COPY --chown="$USER:$GROUP" --chmod=775 pytest.ini manage.py ./
COPY --chown="$USER:$GROUP" --chmod=775 JapariService/ ./JapariService
COPY --chown="$USER:$GROUP" --chmod=775 apps/ ./apps
# </Files setup>


# << Serving >>
# Entry into the eternal work
# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/JapariService/venv/bin/python", "-OO", "-m"]
CMD [ "daphne", \
      "-b", "0.0.0.0", \
      "-p", "80", \
      "--server-name", "jservice_daphne_one", \
      "--http-timeout", "10", \
      "--root-path=/JapariService", \
      "--access-log", "./mnt-logs/serving/daphne-access.log", \
      "--log-fmt", "[%(asctime)s, %(name)s, %(levelname)s]: %(message)s", \
      "JapariService.asgi:app" ]
