import config
from discord.ext import commands,bridge
import discord
import os


def mixedCase(*args):
  """
  Gets all the mixed case combinations of a string

  This function is for in-case sensitive prefixes
  """
  total = []
  import itertools
  for string in args:
    a = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in       string)))
    for x in list(a): total.append(x)

  return list(total)


intents = discord.Intents.all()
intents.members = True
bot = bridge.Bot(command_prefix=config.prefix,intents=intents)


@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f"cul | cul help"))
  le = len(bot.guilds)
  print(bot.user.name,"is READY")
  for i in bot.guilds:
    print("LOGGED IN",i)

  print(f"ONLINE ON {le} Servers")
  



def run_bot(token):
  print("bot ready?")
  
  for filename in os.listdir("./mycogs"):
    if filename.endswith('.py'):
      print(f"{filename } loaded ")
      bot.load_extension(f'mycogs.{filename[:-3]}')

  bot.run(config.auth)


# Run the bot
run_bot(config.auth)