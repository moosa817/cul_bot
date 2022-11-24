import discord
from discord.ext import commands
from time import sleep
class zsetup(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ADDED setup.py")
        client = self.client
        le = len(client.guilds)
        print(client.user.name,"is READY")
        for i in client.guilds:
            print("LOGGED IN",i)
    
        print(f"ONLINE ON {le} Servers")
        await client.change_presence(activity=discord.Game(name=f"cul | cul help"))

async def setup(client):
    await client.add_cog(zsetup(client))