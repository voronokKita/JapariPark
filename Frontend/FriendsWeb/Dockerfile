FROM python:3.11-alpine3.17

LABEL name="FriendsWeb"
LABEL description="Flask application with Gunicorn server."
LABEL author="github.com/voronokKita"
LABEL logs="Mount /FriendsWeb/mnt-logs to get them."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=friends_web_build_pass,env=MYSECRET`"


# <Environment setup>
EXPOSE 80
ENV GUNICORN_PORT=80
ENV BASE_DIR=/FriendsWeb
ENV CONFIGS_DIR=/FriendsWeb/configs
ENV LOGS_DIR=/FriendsWeb/mnt-logs
ENV TEMPLATES_DIR=/FriendsWeb/templates
ENV STATIC_DIR=/FriendsWeb/staticfiles

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
RUN --mount=type=secret,id=friends_web_build_pass,target=/run/secrets/user_pass,required=true \
    echo "$USER:$(cat /run/secrets/user_pass)" | chpasswd

# Add to the administrators group and to the sudoers
RUN addgroup $USER wheel \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo
# </User setup>
# </Environment setup>


# <Files setup>
# Make the base dir and dirs for the logs and templates
RUN mkdir --mode=775 $BASE_DIR \
    && mkdir --mode=775 $LOGS_DIR \
    && mkdir --mode=555 $CONFIGS_DIR \
    && mkdir --mode=555 $TEMPLATES_DIR \
    && mkdir --mode=555 $STATIC_DIR \
    && chown "$UID:$GID" $BASE_DIR $LOGS_DIR $CONFIGS_DIR $TEMPLATES_DIR $STATIC_DIR \
    && touch "$BASE_DIR/indocker"


USER $USER
WORKDIR "$BASE_DIR"
ENV PATH="$BASE_DIR:$PATH"

# Set up a venv and resolve the dependencies
RUN python -m venv "$BASE_DIR/venv"
ENV PATH="$BASE_DIR/venv/bin:$PATH"
COPY --chown="$UID:$GID" --chmod=555 requirements.txt ./
RUN pip install --no-cache -r requirements.txt

COPY --chown="$USER:$GROUP" --chmod=555 manage.py ./
COPY --chown="$USER:$GROUP" --chmod=555 ./manager ./manager
COPY --chown="$USER:$GROUP" --chmod=555 ./FriendsWeb ./FriendsWeb
COPY --chown="$USER:$GROUP" --chmod=555 ./templates $TEMPLATES_DIR
COPY --chown="$USER:$GROUP" --chmod=555 ./staticfiles $STATIC_DIR
COPY --chown="$USER:$GROUP" --chmod=550 ./configs/gunicorn.conf.py $CONFIGS_DIR/gunicorn.conf.py
# </Files setup>


# << Serving >>
# ENTRYPOINT ["tail", "-f", "/dev/null"]  # debug

ENTRYPOINT ["/FriendsWeb/venv/bin/python", "-OO", "-m"]
CMD [ "gunicorn", \
      "--config", "/FriendsWeb/configs/gunicorn.conf.py", \
      "--pythonpath", "/FriendsWeb,/FriendsWeb/venv/bin", \
      "FriendsWeb.wsgi:app" ]
