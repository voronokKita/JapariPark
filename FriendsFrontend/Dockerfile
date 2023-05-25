FROM python:3.11-alpine3.18 as builder

WORKDIR /FriendsFrontend

RUN python -m venv /FriendsFrontend/venv
ENV PATH="/FriendsFrontend/venv/bin:$PATH"

COPY ./requirements.txt .
RUN pip install -r requirements.txt
# </builder>


FROM python:3.11-alpine3.18

WORKDIR /FriendsFrontend

# Add some tools
RUN apk update \
    && apk add --no-cache doas \
    && apk add --no-cache curl \
    && apk add --no-cache vim \
    && echo "permit persist :wheel" >> /etc/doas.d/doas.conf


# Import $ROOT_PASS and $USER_PASS
COPY ./.dockerenv .
RUN source .dockerenv \
    && echo root:$ROOT_PASS | chpasswd


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
# and permissions for the 'doas' to user's group:
RUN echo $USER:$USER_PASS | chpasswd \
    && addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "permit persist :$GID" >> /etc/doas.d/doas.conf


# Copy the project files
COPY ./manage.py .

# Make a docker-flag-file;
# and resolve files permissions:
RUN touch indocker \
    && chown -R $USER:$GID /FriendsFrontend
# skip chmod -R a=rwx /FriendsFrontend


# Make dirs for the future volumes
RUN mkdir tests friends

# Get the venv from builder
COPY --from=builder /FriendsFrontend/venv /FriendsFrontend/venv
ENV PATH="/FriendsFrontend/venv/bin:$PATH"


# Cleaning
RUN unset ROOT_PASS USER_PASS \
    && history -c \
    && rm .dockerenv


# Login as the user
USER luckybot
# don't forget a venv path
ENV PATH="/FriendsFrontend/venv/bin:$PATH"


# Debug
ENTRYPOINT ["tail", "-f", "/dev/null"]
