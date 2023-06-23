FROM python:3.10.2-bullseye
LABEL version="0.1a"
LABEL description="HackMiami Discord Bot"

# Install updates
RUN --mount=target=/var/lib/apt/lists,type=cache \
    --mount=target=/var/cache/apt,type=cache \
    apt-get update \
    && apt-get upgrade -y

WORKDIR /opt/
COPY opt/requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY opt/ /opt/
CMD supervisord -c supervisord.conf
