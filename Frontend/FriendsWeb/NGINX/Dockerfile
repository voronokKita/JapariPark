FROM nginx:1.25-alpine3.17

LABEL name="FriendsWebNginx"
LABEL description="A composite container - part of the FriendsWeb application, \
to host NGINX reverse-proxy."
LABEL author="github.com/voronokKita"
LABEL logs="Mount /FriendsWebNginx/logs to get them."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=friends_web_build_pass,env=MYSECRET`"


# <Environment setup>
EXPOSE 80
ENV NGINX_PORT=80
ENV NGINX_BIN=/usr/sbin/nginx
ENV NGINX_CONF=/etc/nginx

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
RUN addgroup $USER wheel \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo
# </User setup>
# </Environment setup>


# <Files setup>
RUN mkdir --mode=775 $BASE_DIR \
    && mkdir --mode=775 $LOGS_DIR \
    && mkdir --mode=775 $STATIC_DIR \
    && chown "$UID:$GID" $BASE_DIR $LOGS_DIR $STATIC_DIR

WORKDIR "$BASE_DIR"
COPY --chown="$USER:$GROUP" --chmod=775 ./NGINX ./

# Setup NGINX configs
RUN mv "$NGINX_CONF/nginx.conf" "$NGINX_CONF/nginx.conf.backup" \
    && cp "$BASE_DIR/configs/nginx.conf.template" "$NGINX_CONF/nginx.conf" \
    && mkdir --mode=755 "$NGINX_CONF/site-available" \
    && cp "$BASE_DIR/configs/friends.conf.template" "$NGINX_CONF/site-available/friends.conf"

COPY --chown="$USER:$GROUP" --chmod=775 ./staticfiles ./staticfiles
# </Files setup>


# << Serving >>
ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]
