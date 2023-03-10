import discord
from discord.ext import commands
import time
import os
import random


class uwu(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:return
        chance = [1,2,3]
        random.shuffle(chance)
        if chance[0] == 1 or chance[1]==1:
            if message.content.startswith('uwu') or message.content.startswith('UWU')or message.content.startswith('UwU'):
                e = os.getcwd()
                files = os.listdir(e+"/data/uwu")
                
                random.shuffle(files)
                gg = e+'/data/uwu/'+files[0]

                await message.channel.send(file=discord.File(gg))
        else:
            pass




def setup(client):
    client.add_cog(uwu(client))