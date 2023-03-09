from typing import Union
import config
from discord.ext import commands,bridge
import discord
import os
from pymongo import MongoClient


client = MongoClient(config.mongo_str)
db = client.get_database('cul_bot')
records = db.server_info
                

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
bot = bridge.Bot(command_prefix=config.prefix,intents=intents,help_command=None)



@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f"cul | cul help"))
  le = len(bot.guilds)


  print(bot.user.name,"is READY")
  for i in bot.guilds:
    result = records.find_one({"name":str(i)})
    if not result:
      # add data to records
      records.insert_one({"name":str(i),"id":str(i.id),"webhook_link":"","channel_id":""})

    print("LOGGED IN",i)

  print(f"ONLINE ON {le} Servers")



  # server = bot.get_guild(SERVER_ID)
  # channel = server.get_channel(CHANNEL_ID)

  # webhook = await channel.create_webhook(name="waifu")
  # print('Webhook created with URL: {0.url}'.format(webhook))
  
@bot.bridge_command(name="chat_channel",description="Select Channel For Chat Bot")
@discord.option("channel",
        Union[discord.TextChannel, discord.TextChannel],
        # You can specify allowed channel types by passing a union of them like this.
        description="Select a channel",
    )
async def select_channel(
  ctx: discord.ApplicationContext,
  channel: Union[discord.TextChannel, discord.TextChannel],):

  result = records.find_one({"id":str(ctx.guild_id)})
  result = result.get("channel_id")
  if result:
    await ctx.respond(f"<#{result}> is Already Set Please Remove it First if you want to Change channels")
    return
  webhook = await channel.create_webhook(name="Waifu")

  records.update_one({"id":str(ctx.guild_id)},{"$set":{"channel_id":str(channel.id),"webhook_link":str(webhook.url)}})


  await ctx.respond(f"{channel.mention} Has Been Selected as WAIFU chat channel")


@bot.bridge_command(name="remove_channel",description="Remove Channel For Chat Bot")
@discord.option("channel",
        Union[discord.TextChannel, discord.TextChannel],
        # You can specify allowed channel types by passing a union of them like this.
        description="Select a channel",
    )
async def remove_channel(
  ctx: discord.ApplicationContext,
  channel: Union[discord.TextChannel, discord.TextChannel],):

  result = records.find_one({"id":str(ctx.guild_id),"channel_id":str(channel.id)})
  
  if not result:
    await ctx.respond(f"That Channel is'nt selected as a Chat channel do /chat_channel to see")
    return
  
  records.update_one({"id":str(ctx.guild_id)},{"$set":{"channel_id":"","webhook_link":""}})

  await ctx.respond(f"{channel.mention} Has Been Removed from chat channel")





def run_bot(token):
  print("bot ready?")
  
  for filename in os.listdir("./mycogs"):
    if filename.endswith('.py'):
      print(f"{filename } loaded ")
      bot.load_extension(f'mycogs.{filename[:-3]}')

  bot.run(config.auth)


# Run the bot
run_bot(config.auth)