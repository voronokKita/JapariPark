FROM nginx:1.25-alpine3.17

LABEL author="github.com/voronokKita"
LABEL description="A composite container - part of the FriendsWeb application, \
to host NGINX reverse-proxy."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=friends_web_user_pass,env=MYSECRET`"
LABEL logs="Mount /FriendsWebNginx/logs to get them."


# < as root >
# < working with environment >
EXPOSE 8080/tcp
ENV NGINX_PORT=8080
ENV PROXY_PASS="http://friends-web:5000"
ENV PING=/proxy/ping
ENV NGINX_BIN=/usr/sbin/nginx
ENV NGINX_CONF=/etc/nginx
ENV BASE_DIR=/FriendsWebNginx
ENV LOGS_DIR=/FriendsWebNginx/logs
ENV STATIC_DIR=/FriendsWebNginx/staticfiles
ENV USER=luckybot
ENV GROUP=luckybot
ENV UID=1000
ENV GID=1000


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
RUN --mount=type=secret,id=friends_web_user_pass,target=/run/secrets/user_pass,required=true \
    echo "$USER:$(cat /run/secrets/user_pass)" | chpasswd

# Add the user to the administrators group;
# add to the network connections management;
# add user to sudoers;
# set NOPASSWD for the `sudo nginx` command:
RUN addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo \
    && echo "$USER ALL=(ALL) NOPASSWD: $NGINX_BIN" | EDITOR='tee -a' visudo \
    && echo "%$GID ALL=(ALL) NOPASSWD: $NGINX_BIN" | EDITOR='tee -a' visudo


# < working with files >
WORKDIR "$BASE_DIR"

COPY --chown="$USER:$GROUP" --chmod=764 ./NGINX ./

# Resolve file & dir permissions;
# setup NGINX configs:
RUN chown "$USER:$GROUP" "$BASE_DIR" \
    && mv "$NGINX_CONF/nginx.conf" "$NGINX_CONF/nginx.conf.backup" \
    && cp "$BASE_DIR/configs/nginx.conf.template" "$NGINX_CONF/nginx.conf" \
    && mkdir --mode=744 "$NGINX_CONF/site-available" \
    && cp "$BASE_DIR/configs/friends.conf.template" "$NGINX_CONF/site-available/friends.conf"


# < as the user >
USER $USER
ENV PATH="$BASE_DIR:$PATH"

# Make dirs for the logs and secrets
RUN mkdir --mode=777 "$BASE_DIR/logs" \
    && mkdir "$BASE_DIR/secrets"

COPY --chown="$USER:$GROUP" --chmod=764 docker_nginx_run.txt docker-compose.yaml ./
COPY --chown="$USER:$GROUP" --chmod=764 ./staticfiles ./staticfiles


HEALTHCHECK --interval=120s \
            --timeout=5s \
            --retries=2 \
            --start-period=6s \
            CMD curl -f "http://127.0.0.1:8080/proxy/ping" || exit 1

# Entry into the eternal work
# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/usr/bin/sudo", "/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]
