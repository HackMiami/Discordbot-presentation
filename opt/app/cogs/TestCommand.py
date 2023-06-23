import discord
from discord.ext import commands
from configs.config import GUILD_ID


class PrefixTest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name='prefixtest', description='testing prefix commands')
    async def test(self, ctx) -> None:
        await ctx.send('This is a Test.')

    @commands.command(name='argTest', aliases=['argumetentTest'],
                      pass_context=True, description='argumetent_Test prefix commands')
    async def hush(ctx, arg1=None) -> None:
        '''
        !argTest "arg1"
        '''
        if arg1 is None:
            await ctx.send('No argument was given.')
        else:
            await ctx.send(f'This is a argumetent. {arg1}')


async def setup(bot: commands.Bot) -> None:
    # if multiple commands add additional lines.
    await bot.add_cog(PrefixTest(bot), guilds=[discord.Object(id=GUILD_ID)])
