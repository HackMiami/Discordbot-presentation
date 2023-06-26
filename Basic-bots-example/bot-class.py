import discord
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        print('Bot is ready to go!')

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello, I am a Discord bot!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! Latency: {round(self.latency * 1000)}ms')


bot = MyBot(command_prefix='!', intents=discord.Intents.all())

bot.run(token='TOKEN')
