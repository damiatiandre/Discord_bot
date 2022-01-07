import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ">", case_insensitive = True)

@client.event
async def on_ready():
  print('Entramos como {0.user}'.format(client))

@client.command()
async def salve(ctx):
  await ctx.send(f'Salve, salve!  {ctx.author}')


client.run('TOKEN DO BOT')
