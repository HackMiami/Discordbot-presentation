import discord
from discord.ext import commands
from configs.config import GUILD_ID
from libs.logger import logger


class OnJoin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member) -> None:
        bot = self.bot
        new_member_id = member.id
        user = bot.get_user(new_member_id)
        await user.send(f"Welcome to the server {user.name}!")  # send a DM to the user
        logger.info(f"Sent message to {user.name}.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OnJoin(bot), guilds=[discord.Object(id=GUILD_ID)])
