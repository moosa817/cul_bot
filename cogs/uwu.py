import discord
from discord.ext import commands
import time
import os
import random


class uwu(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ADDED uwu.py UwU")

    @commands.Cog.listener()
    async def on_message(self,message):
        chance = [1,2,3]
        random.shuffle(chance)
        if chance[0] == 1 or chance[1]==1:
            client = self.client
            await client.process_commands(message)

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