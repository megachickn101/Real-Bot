import discord
from discord.ext import commands
from discord.utils import get
import pickle
import datetime
import asyncio
import time

intents = discord.Intents.default()
activity = discord.Activity(name='for real', type=discord.ActivityType.watching)
client = commands.Bot(command_prefix = 'r>', activity=activity, intents=intents)
client.remove_command('help')
realcount = pickle.load( open( "real.p", "rb" ) )

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_command_error(ctx, error):
    return error

@client.event
async def on_message(message):
    global realcount
    if "real" in str(message.content):
        realcount = realcount + str(message.content).count("real")
        pickle.dump( realcount, open( "real.p", "wb" ) )
        realcount = pickle.load( open( "real.p", "rb" ) )
    await client.process_commands(message)

def is_it_me(ctx):
	return ctx.author.id == 601881016461819907

@client.command()
@commands.check(is_it_me)
async def shutdown(ctx):
	await client.close()

@client.command()
async def count(ctx):
    global realcount
    await ctx.send(f'The word "real" has been said {realcount} times')

client.run('token')
