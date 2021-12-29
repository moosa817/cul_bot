import discord
from discord.ext import commands

class snipe(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ADDED snipe.py")

    @commands.command()
    async def snipe(self,ctx):
        await ctx.send("A")

def setup(client):
    client.add_cog(snipe(client))