import discord
from discord.ext import commands
from configs.config import GUILD_ID
from cogs.ChildGroup import ChildGroup
from cogs.ParentGroup import ParentGroup


class ParentCog(ParentGroup,
                ChildGroup,
                name="parent", description='parent commands'):
    """All commands and subcommands for the parent command group """


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ParentCog(bot), guilds=[discord.Object(id=GUILD_ID)])
