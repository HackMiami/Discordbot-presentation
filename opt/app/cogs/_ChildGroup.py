# This file is called by ParentCog.py

import discord
from discord import app_commands
from discord.ext import commands


class ChildGroup(commands.GroupCog):

    child = app_commands.Group(name='child', description='child commands')

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # if you dont add the group name to the command name it will be /parent child_command-1
    @child.command(name="child_command-1")
    async def my_child_command_1(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello from sub command 1", ephemeral=True)
