import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
  print("Bot is ready.")

@client.command()
async def Help(ctx):
  await ctx.send(f'Welcome to Pingu')

@client.command()
async def eg(ctx):
  await ctx.send(f'Try asking : ?ping')

@client.command()
async def ping(ctx):
  await ctx.send(f'PONG')

@client.command()
async def ama(ctx,*,question):
  responses = ["Hi", 
                "Hey"]
  await ctx.send(f'Your said: {question} \I says: {random.choice(responses)}')


#client.run('token here')




