import discord
from discord.ext import commands
from configs.config import GUILD_ID
from libs.logger import logger


class OnReady(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.synced = False

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        bot = self.bot
        await self.bot.wait_until_ready()
        if not self.synced:  # check if slash commands have been synced
            logger.info(f"synced {bot.user}.")
            await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
            self.synced = True

        logger.info(f"We have logged in as {bot.user}.")
        logger.info('Connected as: ' + bot.user.name)
        logger.info('Bot id is: %s' % bot.user.id)
        logger.info('Current Member count: %s' % len(list(bot.get_all_members())))
        logger.info('Current Channel count: %s' % len(list(bot.get_all_channels())))
        logger.info('Cmd Prefix: ' + bot.command_prefix)
        logger.info('------')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OnReady(bot), guilds=[discord.Object(id=GUILD_ID)])
