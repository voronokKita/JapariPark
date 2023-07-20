FROM nginx:1.25-alpine3.17

LABEL name="FriendsWebNginx"
LABEL description="A composite container - part of the FriendsWeb application, \
to host NGINX reverse-proxy."
LABEL author="github.com/voronokKita"
LABEL logs="Mount /FriendsWebNginx/mnt-logs to get them."
LABEL secrets="Needs BuildX or BuildKit, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=friends_web_build_pass,env=MYSECRET`"


# <Environment setup>
EXPOSE 8080
EXPOSE 80
ENV INTERNAL_PORT=8080
ENV EXTERNAL_PORT=80

ENV NGINX_BIN=/usr/sbin/nginx
ENV NGINX_DIR=/etc/nginx/

ENV BASE_DIR=/FriendsWebNginx
ENV LOGS_DIR=/FriendsWebNginx/mnt-logs
ENV STATIC_DIR=/FriendsWebNginx/staticfiles

ENV USER=luckybot
ENV GROUP=luckybot
ENV UID=1000
ENV GID=1000


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
# set NOPASSWD for the `sudo nginx` command to the user
RUN addgroup $USER wheel \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo \
    && echo "$USER ALL=(ALL) NOPASSWD: $NGINX_BIN" | EDITOR='tee -a' visudo \
    && echo "%$GID ALL=(ALL) NOPASSWD: $NGINX_BIN" | EDITOR='tee -a' visudo
# </User setup>
# </Environment setup>


# <Files setup>
RUN chmod -R 755 $NGINX_DIR \
    && chown -R "$UID:$GID" $NGINX_DIR \
    && mv $NGINX_DIR/nginx.conf $NGINX_DIR/nginx.conf.backup \
    && mkdir --mode=755 $NGINX_DIR/site-available \
    \
    && mkdir --mode=775 $BASE_DIR \
    && mkdir --mode=775 $LOGS_DIR \
    && chown "$UID:$GID" $BASE_DIR $LOGS_DIR


WORKDIR "$BASE_DIR"
COPY --chown="$USER:$GROUP" --chmod=755 ./NGINX/ping.html ./ping.html
COPY --chown="$USER:$GROUP" --chmod=555 ./NGINX/configs/nginx.conf $NGINX_DIR/nginx.conf
COPY --chown="$USER:$GROUP" --chmod=555 ./NGINX/configs/friends.conf $NGINX_DIR/site-available/friends.conf
COPY --chown="$USER:$GROUP" --chmod=555 ./NGINX/configs/internal_api.conf $NGINX_DIR/site-available/internal_api.conf

COPY --chown="$USER:$GROUP" --chmod=555 ./staticfiles $STATIC_DIR
# </Files setup>


# << Serving >>
USER $USER
ENV PATH="$BASE_DIR:$PATH"

ENTRYPOINT ["/usr/bin/sudo", "/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]
