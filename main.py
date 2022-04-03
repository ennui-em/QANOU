import discord
from discord.ext import commands

intents=discord.Intents.all()
bot=commands.Bot(command_prefix=".", intents=intents)
bot.remove_command("help")

developer= ID
Developer= ID

bot.load_extension("main2")
bot.load_extension("command")
bot.load_extension("manage")

bot.run("TOKEN")
