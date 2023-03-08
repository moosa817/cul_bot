import discord
from discord.ext import commands
import random
import config
from pymongo import MongoClient
# <33
client = MongoClient(config.mongo_str)
db = client.get_database('cul_bot')
records = db.text_stuff
                

class text(commands.Cog):
    def __init__(self,client):
        
        self.client = client


    @commands.Cog.listener()
    async def on_message(self,message):
        results = records.find({})
        names = []
        txts = []
        for i in results:
            names.append(i.get("name"))
            txts.append(i.get("text"))

        for name in names:
            if message.content.startswith(name) or message.content.startswith(name.upper()) or message.content.startswith(name.lower()) or message.content.startswith(name.capitalize()):
                index = names.index(name)
                txt = txts[index]

                await message.channel.send(txt,reference=message)                
           

def setup(client):
    client.add_cog(text(client))