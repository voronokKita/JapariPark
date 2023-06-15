# <builder>
FROM python:3.11-alpine3.18 as builder

WORKDIR /building

RUN python -m venv /building/venv

ENV PATH="/building/venv/bin:$PATH"

COPY requirements.txt ./

RUN pip install --no-cache -r requirements.txt
# </builder>



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
# resolve file & dir permissions;
# touch an indocker flag-file:
COPY .dockerenv ./
RUN source .dockerenv \
    && echo "$USER:$USER_PASS" | chpasswd \
    && addgroup $USER wheel \
    && addgroup $USER netdev \
    && echo "$USER ALL=(ALL) ALL" | EDITOR='tee -a' visudo \
    && chown "$USER:$GROUP" "$BASE_DIR" \
    && touch indocker


# Important! Cleaning
RUN unset USER_PASS \
    && history -c \
    && rm .dockerenv


# <---- as user ---->
USER luckybot

# Set up a venv
COPY --from=builder \
     --chown="$USER:$GROUP" \
     /building/venv ./venv

ENV PATH="$BASE_DIR/venv/bin:$PATH"


# Project files
COPY --chown="$USER:$GROUP" --chmod=777 \
     manage.py ./


# Entry into eternal work
# ENTRYPOINT ["tail", "-f", "/dev/null"]

ENTRYPOINT ["/JapariService/venv/bin/python", "-OO", "-m"]
CMD [ "daphne", \
      "--root-path=/JapariService", \
      "-b", "0.0.0.0", \
      "-p", "8000", \
      "JapariService.asgi:application" ]
