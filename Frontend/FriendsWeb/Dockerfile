FROM python:3.11-alpine3.17

LABEL author="github.com/voronokKita"
LABEL description="FriendsWeb flask application with Gunicorn server. \
Intended to be used with a reverse proxy."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=user_pass,env=MYSECRET`"
LABEL logs="Mount /FriendsWeb/logs to get them."


# < working with the environment >
ENV BASE_DIR=/FriendsWeb
ENV LOGS_DIR=/FriendsWeb/logs
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
RUN --mount=type=secret,id=user_pass,target=/run/secrets/user_pass \
    echo "$USER:$(cat /run/secrets/user_pass)" | chpasswd

# Add to the administrators group;
# add to the network connections management;
# add user to sudoers:
RUN addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo

USER $USER


# Make the base dir;
# set up a venv;
# touch an indocker flag-file;
# and make the dir for the logs:
WORKDIR "$BASE_DIR"
RUN chown "$USER:$GROUP" "$BASE_DIR" \
    && python -m venv "$BASE_DIR/venv" \
    && touch indocker \
    && mkdir -p --mode=777 "$BASE_DIR/logs"

ENV PATH="$BASE_DIR/venv/bin:$PATH"

# Resolve dependencies
COPY --chown="$USER:$GROUP" --chmod=444 requirements.txt ./
RUN pip install --no-cache -r requirements.txt


# < working with files >
COPY --chown="$USER:$GROUP" --chmod=444 Dockerfile manage.py  ./
COPY --chown="$USER:$GROUP" --chmod=444 ./helpers  ./helpers
COPY --chown="$USER:$GROUP" --chmod=444 ./templates  ./templates
COPY --chown="$USER:$GROUP" --chmod=444 ./friends  ./friends
COPY --chown="$USER:$GROUP" --chmod=444 ./tests  ./tests


# Entry into eternal work
# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/FriendsWeb/venv/bin/python", "-OO", "-m"]
CMD [ "gunicorn", \
      "friends.wsgi:app", \
      "-w", "2", \
      "--bind", "0.0.0.0:5000" ]
