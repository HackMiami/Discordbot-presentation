import discord
from discord.ext import commands
from configs.config import GUILD_ID
from cogs._ChildGroup import ChildGroup
from cogs._ParentGroup import ParentGroup


# Here we are inheriting from two classes ParentGroup and ChildGroup to create a new class ParentCog
# This is an example of breaking up a large cog into smaller cogs and then combining them into a single cog under /parent
# /parent subcommand-1
# /parent child child_command-1  - child is a group of subcommands
# Since parent and child are both groups you "can not" add a third group /parent child grandchild grandchild_command-1 - this will not work that I know of
class ParentCog(ParentGroup,
                ChildGroup,
                name="parent", description='parent commands'):
    """All commands and subcommands for the parent command group """


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ParentCog(bot), guilds=[discord.Object(id=GUILD_ID)])
