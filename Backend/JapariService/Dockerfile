FROM python:3.11-alpine3.17

LABEL author="github.com/voronokKita"
LABEL description="The Backend Django application with Daphne server."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=japari_service_user_pass,env=MYSECRET`"
LABEL logs="Mount /JapariService/logs to get them."


# < as root >
# < working with the environment >
EXPOSE 8000/tcp
ENV DAPHNE_PORT=8000
ENV BASE_DIR=/JapariService
ENV LOGS_DIR=/JapariService/logs
ENV GROUP=luckybot
ENV USER=luckybot
ENV GID=1000
ENV UID=1000


# Add some tools and sudo
RUN apk update \
    && apk add --no-cache \
        sudo \
        curl \
        vim \
        coreutils \
    && echo "%wheel ALL=(ALL) ALL" | EDITOR='tee -a' visudo


# Set up a new user & group
RUN addgroup $GROUP --gid $GID \
    && adduser \
        --disabled-password \
        --no-create-home \
        --gecos "" \
        --ingroup $GROUP \
        --uid $UID \
        $USER

# Setup user's password, requires BuildX or BuildKit
RUN --mount=type=secret,id=japari_service_user_pass,target=/run/secrets/user_pass,required=true \
    echo "$USER:$(cat /run/secrets/user_pass)" | chpasswd

# Add to the administrators group;
# add to the network connections management;
# add user to sudoers:
RUN addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo


# < as the user >
USER $USER

# Make the base dir;
# set up a venv:
WORKDIR "$BASE_DIR"
RUN chown "$USER:$GROUP" "$BASE_DIR" \
    && python -m venv "$BASE_DIR/venv"

ENV PATH="$BASE_DIR/venv/bin:$BASE_DIR:$PATH"

# Resolve dependencies
COPY --chown="$USER:$GROUP" --chmod=764 Pipfile requirements.txt ./
RUN pip install --no-cache -r requirements.txt


# < working with files >
# Touch an indocker flag-file;
# and make dirs for the logs and secrets:
RUN touch indocker \
    && mkdir --mode=777 "$BASE_DIR/logs" \
    && mkdir "$BASE_DIR/secrets"

COPY --chown="$USER:$GROUP" --chmod=764 \
     Dockerfile docker_run.txt docker-compose.yaml manage.py ./
COPY --chown="$USER:$GROUP" --chmod=764 ./JapariService ./JapariService
COPY --chown="$USER:$GROUP" --chmod=764 ./helpers ./helpers
COPY --chown="$USER:$GROUP" --chmod=764 ./apps ./apps


HEALTHCHECK --interval=120s \
            --timeout=5s \
            --retries=2 \
            --start-period=6s \
            CMD curl -f "http://127.0.0.1:8000/ping" || exit 1

# Entry into the eternal work
# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/JapariService/venv/bin/python", "-OO", "-m"]
CMD [ "daphne", \
      "--root-path=/JapariService", \
      "-b", "::", \
      "-p", "8000", \
      "JapariService.asgi:application" ]
