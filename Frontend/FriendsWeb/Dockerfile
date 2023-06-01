FROM python:3.11-alpine3.18 as builder

WORKDIR /FriendsWeb

RUN python -m venv /FriendsWeb/venv
ENV PATH="/FriendsWeb/venv/bin:$PATH"

COPY ./requirements.txt .
RUN pip install -r requirements.txt
# </builder>


FROM python:3.11-alpine3.18

WORKDIR /FriendsWeb

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
    && chown -R $USER:$GID /FriendsWeb
# chmod -R a=rwx /FriendsWeb


# Make dirs for the future volumes
RUN mkdir tests friends

# Get the venv from builder
COPY --from=builder /FriendsWeb/venv /FriendsWeb/venv
ENV PATH="/FriendsWeb/venv/bin:$PATH"


# !Important - Cleaning
RUN unset ROOT_PASS USER_PASS \
    && history -c \
    && rm .dockerenv


# Login as the user
USER luckybot
# don't forget the venv path
ENV PATH="/FriendsWeb/venv/bin:$PATH"


# ~debug~ ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/bin/sh", "-c", "python manage.py test ./tests/base && python -OO manage.py"]
