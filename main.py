import discord
from discord.ext import commands
import os
import config

def mixedCase(*args):
  """
  Gets all the mixed case combinations of a string

  This function is for in-case sensitive prefixes
  """
  total = []
  import itertools
  for string in args:
    a = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in string)))
    for x in list(a): total.append(x)

  return list(total)




client = commands.Bot(case_insensitive=True,command_prefix=mixedCase(config.prefix))
client.remove_command('help')

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(config.auth)