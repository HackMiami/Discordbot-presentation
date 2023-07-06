import discord
from discord.ext import commands
from configs.config import GUILD_ID
from .ParentRoot import ParentRoot
from .ChildGroup import ChildGroup


class CogModule(ParentRoot,
                ChildGroup,
                name="CogModule", description='CogModule commands'):
    """All commands and subcommands for the parent command group """


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CogModule(bot), guilds=[discord.Object(id=GUILD_ID)])
