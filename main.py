import config
from discord.ext import commands
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
bot = commands.Bot(command_prefix=config.prefix,intents=intents)



@bot.tree.command(name="hello")
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message("i need badge")




@bot.event
async def on_ready():
    print("bot ready?")
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            print(f"{filename } loaded ")
            await bot.load_extension(f'cogs.{filename[:-3]}')
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(e)

# Run the bot
bot.run(config.auth)