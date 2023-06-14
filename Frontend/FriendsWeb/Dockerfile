FROM nginx:1.25.0-alpine3.17

# <-------- as root -------->
ENV NGINX_BIN=/usr/sbin/nginx
ENV NGINX_CONF=/etc/nginx
WORKDIR /FriendsWeb


# Add some tools and sudo;
# install python:
ENV PYTHONUNBUFFERED=1
RUN apk update \
    && apk add --no-cache \
        sudo \
        curl \
        vim \
        openssl \
        ca-certificates \
        coreutils \
        python3 \
    && ln -sf python3 /usr/bin/python \
    && python -m ensurepip \
    && pip3 install --no-cache --upgrade pip setuptools wheel


# Set up a new user & group
ENV GID=1000
ENV UID=1000
ENV USER=luckybot
ENV GROUP=luckybot

RUN addgroup $GROUP --gid $GID \
    && adduser \
        --disabled-password \
        --no-create-home \
        --gecos "" \
        --ingroup $GROUP \
        --uid $UID \
        $USER


# Import $USER_PASS;
# setup user's password;
# add to the administrators group;
# add to the network connections management;
# set NOPASSWD for the `sudo nginx` command;
# resolve file & dir permissions:
COPY .dockerenv ./
RUN source .dockerenv \
    && echo "$USER:$USER_PASS" | chpasswd \
    && addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "$USER ALL=(ALL) NOPASSWD: $NGINX_BIN" >> /etc/sudoers \
    && echo "%$GID ALL=(ALL) NOPASSWD: $NGINX_BIN" >> /etc/sudoers \
    && chmod -R 777 "$NGINX_CONF" \
    && chown -R "$USER:$GROUP" /FriendsWeb

# Important! Cleaning
RUN unset USER_PASS \
    && history -c \
    && rm .dockerenv


# <---- as user ---->
USER luckybot

# Set up a venv and touch an indocker flag-file
RUN python -m venv /FriendsWeb/venv \
    && touch indocker
ENV PATH="/FriendsWeb/venv/bin:$PATH"

# Resolve dependencies
COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt


# <---- Project files ---->
COPY manage.py config.py base_dir.py ./


# Entry into eternal work
ENTRYPOINT ["tail", "-f", "/dev/null"]

# Entry with base tests
# ENTRYPOINT ["/bin/sh", "-c", "python manage.py test && python -OO manage.py dev"]
