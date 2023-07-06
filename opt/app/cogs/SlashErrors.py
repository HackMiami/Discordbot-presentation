import discord
from discord import app_commands, Interaction
from discord.ext import commands
from configs.config import GUILD_ID
from libs.logger import logger


# Custom Error Class for Slash Commands to handle errors
# return a message to the user
class CustomError(app_commands.AppCommandError):
    def __init__(self, message: str = None) -> None:
        super().__init__(message or 'An unknown error occurred.')


# This is a custom check decorator that checks if the command is executed in the correct channel.
def in_this_channel(chan_name) -> bool:
    async def actual_check(interaction: Interaction):
        if interaction.channel.name == chan_name:
            # Add logger here
            return True
        else:
            await interaction.response.send_message("Command excuted in wrong channel")
            # Add logger here
            logger.error("Command excuted in wrong channel")
            logger.error(f"interaction.channel.name: {interaction.channel.name}")
            logger.error(f"User: {interaction.user.name}")
            logger.error(f"User ID: {interaction.user.id}")
            logger.error(f"Command: {interaction.data['name']}")
            logger.error(f"Command Args: {interaction.data['options']}")
            raise CustomError("Command excuted in wrong channel")

    # returning the check
    return app_commands.check(actual_check)


class SlashGroup(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    # This is a global error handler for the cog.
    async def cog_app_command_error(self, interaction: Interaction, error: app_commands.AppCommandError) -> None:
        pass

    # @app_commands.checks.has_any_role(000000000000000, 000000000000001) #  Checks if the invoker has any of the specified roles.
    # @app_commands.check.has_role(00000000000000000000)  #  Checks if the invoker has the specified role.
    # @app_commands.check.is_owner() #  Checks if the invoker is the owner of the bot.
    # @app_commands.check.has_permissions(manage_channels=True) #  Checks if the invoker has the specified permissions.
    @in_this_channel('some_missing_channel')
    @app_commands.command(name="Error_cmd")
    async def my_sub_command_1(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("You will not see this message.", ephemeral=True)

    # This is a local error handler for the command.
    @my_sub_command_1.error
    async def setup_events_error(self, interaction: Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CheckFailure):
            logger.info(f"setup_events_error: {error}")
            logger.info(dir(error))
            return
        raise error


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashGroup(bot), guilds=[discord.Object(id=GUILD_ID)])
