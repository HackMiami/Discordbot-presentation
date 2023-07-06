import discord
from discord import app_commands
from discord.ext import commands
from configs.config import GUILD_ID


# Slash Group Test
# This is an example of grouping commands under /parent that has two sub commands /parent sub-1 and /parent sub-2
class SlashGroup(commands.GroupCog, name="parent0"):
    # This is an example of grouping commands under /parent that has a sub command /parent child child-1
    child = app_commands.Group(name='child0', description='child commands')

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @child.command(name="child0-cmd")
    async def child_sub_command_1(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello from child command 1", ephemeral=True)

    @app_commands.command(name="parent0-cmd")
    async def my_sub_command_1(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello from sub command 1", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashGroup(bot), guilds=[discord.Object(id=GUILD_ID)])
