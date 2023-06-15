FROM nginx:1.25-alpine3.17

LABEL author="https://github.com/voronokKita"
LABEL description="A container with a user and NGINX reverse-proxy. \
You need to provide a password: `docker build --build-arg USER_PASS=something`."


# <----- working with environment ----->
ENV NGINX_BIN=/usr/sbin/nginx
ENV NGINX_CONF=/etc/nginx
ENV BASE_DIR=/FriendsWebNginx


# Add some tools and sudo;
RUN apk update \
    && apk add --no-cache \
        sudo \
        curl \
        vim \
    && echo "%wheel ALL=(ALL) ALL" | EDITOR='tee -a' visudo


# Set up a new user & group
ENV USER=luckybot
ENV GROUP=luckybot
ENV UID=1000
ENV GID=1000

RUN addgroup $GROUP --gid $GID \
    && adduser \
        --disabled-password \
        --no-create-home \
        --gecos "" \
        --ingroup $GROUP \
        --uid $UID \
        $USER

# Setup user's password;
# add to the administrators group;
# add to the network connections management;
# add user to sudoers;
# set NOPASSWD for the `sudo nginx` command:
RUN echo "$USER:$USER_PASS" | chpasswd \
    && addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo \
    && echo "$USER ALL=(ALL) NOPASSWD: $NGINX_BIN" | EDITOR='tee -a' visudo \
    && echo "%$GID ALL=(ALL) NOPASSWD: $NGINX_BIN" | EDITOR='tee -a' visudo


# <----- working with files ----->
# Copy the files
WORKDIR "$BASE_DIR"
COPY --chown="$USER:$GROUP" --chmod=777 . .

# Resolve file & dir permissions;
# and setup NGINX configs:
RUN mkdir -p "$BASE_DIR/logs" \
    && chown -R "$USER:$GROUP" "$BASE_DIR" \
    && chmod -R 777 "$BASE_DIR" \
    && cp "$NGINX_CONF/nginx.conf" "$NGINX_CONF/nginx.conf.backup" \
    && cp "$BASE_DIR/configs/nginx.conf.template" "$NGINX_CONF/nginx.conf" \
    && mkdir -p "$NGINX_CONF/site-available" \
    && cp "$BASE_DIR/configs/friends.conf.template" "$NGINX_CONF/site-available/friends.conf"


USER luckybot

# Entry into eternal work
# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/usr/bin/sudo", "/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]
