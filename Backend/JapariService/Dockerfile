FROM python:3.11-alpine3.18

# <-------- as root -------->
ENV BASE_DIR=/JapariService
WORKDIR /JapariService


# Add some tools and sudo
RUN apk update \
    && apk add --no-cache \
        sudo \
        curl \
        vim \
    && pip3 install --no-cache --upgrade \
        pip \
        setuptools \
        wheel \
    && echo "%wheel ALL=(ALL) ALL" | EDITOR='tee -a' visudo


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
# add user to sudoers;
# resolve file & dir permissions:
COPY .dockerenv ./
RUN source .dockerenv \
    && echo "$USER:$USER_PASS" | chpasswd \
    && addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo \
    && chown "$USER:$GROUP" "$BASE_DIR"


# Important! Cleaning
RUN unset USER_PASS \
    && history -c \
    && rm .dockerenv


# <---- as user ---->
USER luckybot

# Set up a venv and touch an indocker flag-file
RUN python -m venv "$BASE_DIR"/venv \
    && touch indocker
ENV PATH="$BASE_DIR/venv/bin:$PATH"


# Resolve dependencies
COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt


# <---- Project files ---->
COPY --chown="$USER:$GROUP" --chmod=777 manage.py ./


# Entry into eternal work
ENTRYPOINT ["tail", "-f", "/dev/null"]
