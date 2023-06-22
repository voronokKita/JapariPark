FROM python:3.11-alpine3.17

LABEL author="github.com/voronokKita"
LABEL description="The Flask application with Gunicorn server. \
Intended to be used with a reverse proxy."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=friends_web_user_pass,env=MYSECRET`"
LABEL logs="Mount /FriendsWeb/logs to get them."


# < as root >
# < working with the environment >
ENV BASE_DIR=/FriendsWeb
ENV LOGS_DIR=/FriendsWeb/logs
ENV HTML_DIR=/FriendsWeb/templates
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
RUN --mount=type=secret,id=friends_web_user_pass,target=/run/secrets/user_pass,required=true \
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
     Dockerfile docker-compose.yaml manage.py ./
COPY --chown="$USER:$GROUP" --chmod=764 ./friends ./friends
COPY --chown="$USER:$GROUP" --chmod=764 ./helpers ./helpers
COPY --chown="$USER:$GROUP" --chmod=764 ./templates ./templates
COPY --chown="$USER:$GROUP" --chmod=764 ./tests ./tests


# Serving
ENV GUNICORN_PORT=80

# Entry into the eternal work
# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/FriendsWeb/venv/bin/python", "-OO", "-m"]
CMD [ "gunicorn", \
      "friends.wsgi:app", \
      "-w", "2", \
      "--bind", "0.0.0.0:80" ]
