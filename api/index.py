import os

import discord

from dotnet import load_dotenv

from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()

activity = discord.Game(name="Лор мой пупсик")

bot = commands.Bot(command_prefix="!", intents = intents, status=discord.Status.idle)

@bot.command

async def cleanraid(ctx,name):

    await ctx.send ("Очистка рейда 🌿")

    for channel in bot.get_all_channels():

        if channel.name == name:

            await channel.delete()

    await ctx.send("Рейд очищен 💫")

bot.run(os.getenv("token"))
