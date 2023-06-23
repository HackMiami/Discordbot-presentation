import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('Bot is ready to go!')


@bot.command()
async def hello(ctx) -> None:
    await ctx.send('Hello, I am a Discord bot!')


@bot.command()
async def ping(ctx) -> None:
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

bot.run('YOUR_BOT_TOKEN')
