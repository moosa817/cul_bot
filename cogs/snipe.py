import discord
from discord.ext import commands
from time import sleep

snipe_message_author = {}
snipe_message_content = {}

class snipe(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ADDED snipe.py")

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content

        # del snipe_message_author[message.channel.id]
        # del snipe_message_content[message.channel.id]
 
    @commands.command()
    async def snipe(self,ctx):
        channel = ctx.channel 
        try:
            snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
            snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
            await ctx.send(embed = snipeEmbed)
        except:
            await ctx.send(f"There are no deleted messages in #{channel.name}")

def setup(client):
    client.add_cog(snipe(client))