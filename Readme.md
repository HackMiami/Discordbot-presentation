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

#### Large GoupCogs

How break up large goupcogs or add group cog from other py files?


`/parent child child_cmd-1`

```
app/
├── cogs/
├── ChildGroup.py
├── ParentGroup.py
├── ParentCog.py
└── main.py
```

`main.py`
```python
import discord
from discord.ext import commands
from configs.config import MODS, TOKEN, PREFIX
from libs.logger import logger

PREFIX = '>'
TOKEN = 'TOKEN'
MODS = ['ParentCog']

class MyBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=PREFIX, intents=discord.Intents.all(), help_command=None)

    async def setup_hook(self) -> None:
        for mod in MODS:
            logger.info(f'Loading {mod}')
            await self.load_extension(f'cogs.{mod}')  # name of module

    async def close(self) -> None:
        await super().close()


bot = MyBot()
bot.run(TOKEN)
```

`ParentCog.py`
```python
import discord
from discord.ext import commands
from configs.config import GUILD_ID
from cogs.ChildGroup import ChildGroup
from cogs.ParentGroup import ParentGroup

GUILD_ID = 000000000000000000

class ParentCog(ParentGroup,
                ChildGroup,
                name="parent", description='parent commands'):
    """All commands and subcommands for the parent command group """


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ParentCog(bot), guilds=[discord.Object(id=GUILD_ID)])

```



`ParentGroup.py`
```python
import discord
from discord import app_commands
from discord.ext import commands


class ParentGroup(commands.GroupCog, name="someparent"):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="parent_command-1")
    async def my_sub_command_1(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello from parent_command 1", ephemeral=True)

```



`ChildGroup.py`
```python
import discord
from discord import app_commands
from discord.ext import commands


class ChildGroup(commands.GroupCog):

    child = app_commands.Group(name='child', description='child commands')

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @child.command(name="child_command-1")
    async def my_child_command_1(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello from sub command 1", ephemeral=True)


```
