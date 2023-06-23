# Hackmiami - Discord bot presentation

update TOKEN, GUILD_ID and ROLE_ID in config/config.py


## Other examples from the developer
https://github.com/Rapptz/discord.py/tree/master/examples


Joing the discord.py server
https://discord.gg/dpy


## With Docker compose

docker compose build
docker compose up -d
docker compose logs

### if you want to jump into the image to test
docker compose exec -it bot bash

## Without docker compose

docker build -f Docker/Dockerfile -t -t doscord-bot:latest .
docket run -rm doscord-bot -v logs:/var/logs


## Without docker

```
pip install requirements.txt
python main.py
```
