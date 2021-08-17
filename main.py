import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix = "!", intents=discord.Intents.all(), case_insensitive = True)
@client.event
async def on_ready():
    print("Lets gooo")

@client.event
async def on_member_join(member):
    channel = client.get_channel(875706600273350698)
    await channel.send("Hello")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(875706600273350698)
    await channel.send("Bye")

@client.command()
async def hello(ctx):
    await ctx.send("Hello This is a sample bot by code")
@client.command()
async def bye(ctx):
    await ctx.send("Life is Epic!!")


client.run('ODc1NzA3MTg1MTk0MjMzODk2.YRZb3g.o7QRKPbLx6nU99AibG9FRti8c6M')