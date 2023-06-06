FROM nginx:1.25.0-alpine3.17

# Add some tools and sudo
RUN apk update \
    && apk add --no-cache sudo \
    && apk add --no-cache curl \
    && apk add --no-cache vim \
    && apk add --no-cache openssl \
    && apk add --no-cache ca-certificates \
    && apk add --no-cache coreutils


# Install python
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache python3 \
    && ln -sf python3 /usr/bin/python \
    && python -m ensurepip \
    && pip3 install --no-cache --upgrade pip setuptools wheel


WORKDIR /FriendsWeb

# Import $ROOT_PASS and $USER_PASS
COPY ./.dockerenv ./
RUN source .dockerenv \
    && echo "root:$ROOT_PASS" | chpasswd


# Set up a new user
ENV GID=1001
ENV UID=1000
ENV USER=luckybot

RUN addgroup $GID \
    && adduser \
        --disabled-password \
        --no-create-home \
        --gecos "" \
        --ingroup $GID \
        --uid $UID \
        $USER

# Setup user's password;
# add to the administrators group;
# add to the network connections management;
# and permissions for the `sudo nginx`:
# `which nginx` returns `/usr/sbin/nginx`
RUN echo "$USER:$USER_PASS" | chpasswd \
    && addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "$USER ALL=(ALL) NOPASSWD: /usr/sbin/nginx" >> /etc/sudoers \
    && echo "%$GID ALL=(ALL) NOPASSWD: /usr/sbin/nginx" >> /etc/sudoers


# Copy the project files
COPY requirements.txt manage.py config.py base_dir.py ./

# Touch a docker-flag-file;
# and resolve files permissions;
# Resolve permissions for the nginx-config dir,
# required for automatic config writing...
# ~~~~~~~~~~~~~~~~~ Note ~~~~~~~~~~~~~~~~~~~~ #
# The documentation indicates that configs    #
# can be in the other two directories,        #
# which can create additional problems        #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
RUN touch indocker \
    && chown -R "$USER:$GID" /FriendsWeb \
    && chmod -R 777 /etc/nginx

# Set up a venv and resolve dependencies
RUN python -m venv /FriendsWeb/venv
ENV PATH="/FriendsWeb/venv/bin:$PATH"

RUN pip install --no-cache -r requirements.txt


# !Important - Cleaning
RUN unset ROOT_PASS USER_PASS \
    && history -c \
    && rm .dockerenv


# Login as the user
USER luckybot
# don't forget the venv path
ENV PATH="/FriendsWeb/venv/bin:$PATH"


# ~debug~
ENTRYPOINT ["tail", "-f", "/dev/null"]

# Entry with base tests
#ENTRYPOINT ["/bin/sh", "-c", "python manage.py test && python -OO manage.py dev"]
