import discord
from discord.ext import commands
from configs.config import MODS, TOKEN, PREFIX
from libs.logger import logger


class HackMiamiBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=PREFIX, intents=discord.Intents.all(), help_command=None)

    async def setup_hook(self) -> None:
        for mod in MODS:
            logger.info(f'Loading {mod}')
            await self.load_extension(f'cogs.{mod}')  # name of module

    async def close(self) -> None:
        await super().close()


bot = HackMiamiBot()
bot.run(TOKEN)
