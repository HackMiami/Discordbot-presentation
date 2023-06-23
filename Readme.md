# Hackmiami - Discord bot presentation

update token and GUILD_ID in config/config.py


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



hackmiami-discord/
├── Docker/
│   └── Dockerfile
├── docker-compose.yml
├── logs/
│   ├── bot.log
│   └── supervisord.log
├── opt/
│   ├── app/
│   │   ├── cogs/
│   │   │   ├── BotHelp.py
│   │   │   ├── OnJoin.py
│   │   │   ├── OnReaction.py
│   │   │   ├── OnReady.py
│   │   │   ├── SlashTest.py
│   │   │   └── TestCommand.py
│   │   ├── configs/
│   │   │   └── config.py
│   │   ├── libs/
│   │   │   └── logger.py
│   │   └── main.py
│   ├── requirements.txt
│   └── supervisord.conf
└── Readme.md
