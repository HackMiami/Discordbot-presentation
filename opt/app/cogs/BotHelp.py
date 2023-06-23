import discord
from discord.ext import commands
from configs.config import GUILD_ID


class BotHelp(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name='help', description='help massage')
    async def help_commands(self, ctx) -> None:
        '''Custom Help'''
        prefix = self.bot.command_prefix

        message = f'''
        Commands
        --------------------
        **Get a list of all commands**

        `{prefix} help`
        '''

        message_list = []
        buff = ''
        for line in message.splitlines():
            line += '\n'
            lines_len = len(buff) + len(line)
            if lines_len <= 1500:
                buff = buff + line
            else:
                message_list.append(buff + '```')
                buff = '```' + line
        message_list.append(buff)
        for message in message_list:
            await ctx.author.send(message)
        await ctx.send('You Got Mail!')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BotHelp(bot), guilds=[discord.Object(id=GUILD_ID)])
