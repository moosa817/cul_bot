import discord
from discord.ext import commands

class snipe(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ADDED snipe.py")

def setup(client):
    client.add_cog(snipe(client))