FROM nginx:1.25-alpine3.17

LABEL author="github.com/voronokKita"
LABEL description="A composite container - part of the FriendsWeb application, \
to host NGINX reverse-proxy."
LABEL secrets="Needs BuildX or BuildKit on, like: \
`$ MYSECRET=qwerty DOCKER_BUILDKIT=1 docker build --secret id=user_pass,env=MYSECRET`"
LABEL context="The parent directory, where the staticfiles are originated."
LABEL logs="Mount /FriendsWebNginx/logs to get them."


# < working with environment >
EXPOSE 8080/tcp
ENV NGINX_BIN=/usr/sbin/nginx
ENV NGINX_CONF=/etc/nginx
ENV BASE_DIR=/FriendsWebNginx
ENV LOGS_DIR=/FriendsWebNginx/logs
ENV USER=luckybot
ENV GROUP=luckybot
ENV UID=1000
ENV GID=1000


# Add some tools and sudo;
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
COPY --chown="$USER:$GROUP" --chmod=444 ./NGINX ./

# Resolve file & dir permissions;
# make a dir for the logs;
# and setup NGINX configs:
RUN chown "$USER:$GROUP" "$BASE_DIR" \
    && mkdir -p --mode=777 "$BASE_DIR/logs" \
    && mv "$NGINX_CONF/nginx.conf" "$NGINX_CONF/nginx.conf.backup" \
    && cp "$BASE_DIR/configs/nginx.conf.template" "$NGINX_CONF/nginx.conf" \
    && mkdir -p --mode=744 "$NGINX_CONF/site-available" \
    && cp "$BASE_DIR/configs/friends.conf.template" "$NGINX_CONF/site-available/friends.conf"

COPY --chown="$USER:$GROUP" --chmod=444 ./staticfiles ./staticfiles


USER luckybot

# Entry into eternal work
# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/usr/bin/sudo", "/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]
