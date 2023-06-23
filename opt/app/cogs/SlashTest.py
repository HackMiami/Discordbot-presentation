import discord
from discord import app_commands, Interaction
from discord.ext import commands
from discord.app_commands import AppCommandError, Choice
from configs.config import GUILD_ID, ROLE_ID
from libs.logger import logger


def get_image():
    import requests
    from io import BytesIO
    url = 'https://filmymantra.com/wp-content/uploads/2015/06/full33843796.jpg'
    response = requests.get(url)
    response.raise_for_status()  # check for errors
    return BytesIO(response.content)


class SlashTest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name='slashtest', description='testing slash commands')
    async def test(self, interaction: discord.Interaction, name: str, num: int) -> None:
        await interaction.response.send_message(f"I am working {name}, your num is {num}", ephemeral=True)


class ChoiceTest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.checks.has_any_role(ROLE_ID)
    @app_commands.command(name='choicetest', description='testing slash choice commands')
    @app_commands.describe(fruits='fruits to choose from')
    @app_commands.choices(fruits=[
        Choice(name='apple', value=1),
        Choice(name='banana', value=2),
        Choice(name='cherry', value=3),
    ])
    async def choiceTest(self, interaction: discord.Interaction, fruits: Choice[int]) -> None:
        if fruits.value == 1:
            await interaction.response.send_message(f'Yum you like {fruits.name}.')
        elif fruits.value == 2:
            await interaction.response.send_message(f'Yum you like {fruits.name}.')
            image = get_image()
            await interaction.channel.send(file=discord.File(image, 'image.png'))
        else:
            await interaction.response.send_message(f'Your favourite fruit is {fruits.name}.')

    async def cog_app_command_error(self, interaction: Interaction, error: AppCommandError) -> None:
        await interaction.response.send_message(f'ERROR: {error}')
        logger.error(f"This error was handled with options: {error}")


class SlashGroup(commands.GroupCog, name="parent"):
    child = app_commands.Group(name='child', description='child commands')

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @child.command(name="child-1")
    async def child_sub_command_1(self, interaction: discord.Interaction) -> None:
        """ /parent sub-1 """
        await interaction.response.send_message("Hello from child command 1", ephemeral=True)

    @app_commands.command(name="sub-1")
    async def my_sub_command_1(self, interaction: discord.Interaction) -> None:
        """ /parent sub-1 """
        await interaction.response.send_message("Hello from sub command 1", ephemeral=True)

    @app_commands.command(name="sub-2")
    async def my_sub_command_2(self, interaction: discord.Interaction) -> None:
        """ /parent sub-2 """
        await interaction.response.send_message("Hello from sub command 2", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashTest(bot), guilds=[discord.Object(id=GUILD_ID)])
    await bot.add_cog(ChoiceTest(bot), guilds=[discord.Object(id=GUILD_ID)])
    await bot.add_cog(SlashGroup(bot), guilds=[discord.Object(id=GUILD_ID)])
