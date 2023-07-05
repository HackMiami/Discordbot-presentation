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
