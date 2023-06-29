import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
from configs.config import GUILD_ID
import traceback


async def reload_extension(bot: commands.Bot, interaction, cog_name: str) -> None:
    try:
        await bot.reload_extension(cog_name)
        await interaction.channel.send(f"Cog {cog_name} has been reloaded!")
        await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
    except Exception as e:
        await interaction.channel.send(f"Failed to reload cog {cog_name}. Error: {str(e)}")


def get_all_extensions_list() -> list[Choice]:
    import os
    cogs_files_list = []
    for file in os.listdir('cogs'):
        if '_' in file:  # ignore __init__.py and __pycache__
            continue
        cogs_files_list.append(file.replace('.py', ''))
    return [Choice(name=extension, value=extension) for extension in cogs_files_list]


class Admin(commands.GroupCog, name="admin"):
    cog = app_commands.Group(name='cog', description='cog commands')

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @cog.command(name="load")
    @commands.is_owner()
    @app_commands.choices(cog_name=get_all_extensions_list())
    async def load_cog(self, interaction: discord.Interaction, cog_name: str) -> None:
        extensions = [extension for extension in self.bot.extensions]
        if 'cogs.' + cog_name in extensions:
            return await interaction.response.send_message(f"Cog '{cog_name}' is already loaded.", ephemeral=True)

        if cog_name == 'cogs.CogsLoader':
            return await interaction.response.send_message(f"Cog '{cog_name}' cannot be loaded.", ephemeral=True)
        try:
            await self.bot.load_extension(f'cogs.{cog_name}')
            await interaction.response.send_message(f"Cog '{cog_name}' loaded successfully.", ephemeral=True)
            await self.bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        except Exception as e:
            traceback.print_exc()
            await interaction.response.send_message(f"Failed to load cog '{cog_name}': {e}", ephemeral=True)

    @cog.command(name="unload")
    @commands.is_owner()
    @app_commands.choices(cog_name=get_all_extensions_list())
    async def unload_cog(self, interaction: discord.Interaction, cog_name: str):
        extensions = [extension for extension in self.bot.extensions]
        if 'cogs.' + cog_name not in extensions:
            return await interaction.response.send_message(f"Cog '{cog_name}' is not loaded.", ephemeral=True)

        if cog_name == 'cogs.CogsLoader':
            return await interaction.response.send_message(f"Cog '{cog_name}' cannot be unloaded.", ephemeral=True)
        try:
            cog = self.bot.get_cog(cog_name)
            if cog:
                await self.bot.remove_cog(cog)
            await self.bot.unload_extension(f'cogs.{cog_name}')
            await interaction.response.send_message(f"Cog '{cog_name}' unloaded successfully.", ephemeral=True)
            await self.bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        except Exception as e:
            await interaction.response.send_message(f"Failed to unload cog '{cog_name}': {e}", ephemeral=True)

    @cog.command(name="list")
    @commands.is_owner()
    async def list(self, interaction: discord.Interaction):
        extensions = [extension for extension in self.bot.extensions]
        extensions = '\n'.join(extensions)
        message = f"---Loaded cogs---\n{extensions}"
        await interaction.response.send_message(message)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot), guilds=[discord.Object(id=GUILD_ID)])
