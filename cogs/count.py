import discord
from discord.ext import commands

class count(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ADDED count.py")

def setup(client):
    client.add_cog(count(client))