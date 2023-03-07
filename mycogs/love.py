import discord
from discord.ext import commands
import time
import os
import random

# <33
class love(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):

        if message.content.startswith('<33'):
            e = os.getcwd()
            files = os.listdir(e+"/data/loml")
            
            random.shuffle(files)
            gg = e+'/data/loml/'+files[0]
            print(discord.File(gg))
            await message.channel.send(file=discord.File(gg))




def setup(client):
    client.add_cog(love(client))