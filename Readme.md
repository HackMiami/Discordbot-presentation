# Hackmiami - Discord bot presentation

## Presentation
Slides:
- https://docs.google.com/presentation/d/1xCEXvK5QcWgNO2mXJpSJKhHBGgcWbjrS-784hCxUAzI/edit?usp=sharing

- https://github.com/HackMiami/Discordbot-presentation
To use this on your server update TOKEN, GUILD_ID and ROLE_ID in config/config.py

Enjoy and happy programming

## Other examples from the developer
- https://github.com/Rapptz/discord.py/tree/master/examples

- https://discordpy.readthedocs.io/en/latest/index.html

### Other examples
- https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
-
## Discord servers
Joing the discord.py server https://discord.gg/dpy


## With Docker compose

```
docker compose build
docker compose up -d
docker compose logs
```
### if you want to jump into the image to test

```
docker compose exec -it bot bash
```
## Without docker compose

```
docker build -f Docker/Dockerfile -t discord-bot:latest .
docker run --rm -v logs:/var/logs discord-bot
```

## Without docker

#### setup a virtualenv

```
python -m ensurepip
python -m venv .venv
source pyenv/bin/activate
```

#### install requirements and run the bot.
```
pip install -r opt/requirements.txt
python main.py
```
