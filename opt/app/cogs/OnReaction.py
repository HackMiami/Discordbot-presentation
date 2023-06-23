import discord
from discord.ext import commands
from configs.config import GUILD_ID, ROLE_ID
from libs.logger import logger


class SelfRolesMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='selfroles', description='Self assignable roles')
    async def post_message(self, ctx):
        message = await ctx.send("Get this new role by reacting to this message with a thumbs-up!")
        await message.add_reaction("👍")


class OnReaction(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload) -> None:
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        if member.bot:
            logger.info("User is bot.")
            return

        if message.author.id == self.bot.user.id:
            # Check for specific reaction emoji or do something based on the reaction
            if payload.emoji.name == "👍":
                # Perform action when the thumbs-up reaction is added
                await message.channel.send(f"{member.name} liked the message!")
                # the use a role id to add a role to the user
                await member.add_roles(discord.Object(id=ROLE_ID))
                logger.info(f"Added role to {member.name}.")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload) -> None:
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        if member.bot:
            logger.info("User is bot.")
            return

        if message.author.id == self.bot.user.id:
            # Check for specific reaction emoji or do something based on the reaction
            if payload.emoji.name == "👍":
                # Perform action when the thumbs-up reaction is added
                await message.channel.send(f"{member.name} unliked the message!")
                # the use a role id to add a role to the user
                await member.remove_roles(discord.Object(id=ROLE_ID))
                logger.info(f"Removed role from {member.name}.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OnReaction(bot), guilds=[discord.Object(id=GUILD_ID)])
    await bot.add_cog(SelfRolesMessage(bot), guilds=[discord.Object(id=GUILD_ID)])
