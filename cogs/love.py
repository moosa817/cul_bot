import discord
from discord.ext import commands
import time
import os
import random


class love(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ADDED uwu.py UwU")

    @commands.Cog.listener()
    async def on_message(self,message):
        
        client = self.client
        await client.process_commands(message)

        if message.content.startswith('<33'):
            e = os.getcwd()
            files = os.listdir(e+"/data/loml")
            
            random.shuffle(files)
            gg = e+'/data/loml/'+files[0]

            await message.channel.send(file=discord.File(gg))
            time.sleep(4)




def setup(client):
    client.add_cog(love(client))