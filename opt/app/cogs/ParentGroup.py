import discord
from discord import app_commands
from discord.ext import commands


class ParentGroup(commands.GroupCog, name="someparent"):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="parent_command-1")
    async def my_sub_command_1(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello from parent_command 1", ephemeral=True)
