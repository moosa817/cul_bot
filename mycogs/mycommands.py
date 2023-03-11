from discord.ext import commands,bridge
from additional_files import ask
import config
import discord
import discord

# <33
class mycommands(commands.Cog):

    def __init__(self,client):
        self.client = client


    @bridge.bridge_command(description="Math questions/Date Related Questions/random no etc")
    async def ask(self,ctx,question:str):
        await ctx.respond(ask.ask(question,config.rapid_api_key))

    @bridge.bridge_command(description="Help Command")
    async def help(self,ctx):

        
        helpEmbed = embed=discord.Embed(title="Ask Command", description="```/ask <question> OR cul ask <question> ``` Math questions/Date Related Questions/random no etc ")
        embed.add_field(name="Search Command", value="```/search <keyword> <no_of_images> OR cul search <keyword> <no_of_images>``` Search Images With Pinterest", inline=False)
        embed.add_field(name="Snipe Command", value="```/snipe OR cul snipe ``` Bring up Last Message", inline=True)
        embed.add_field(name="Add Waifu Channel", value="```/chat_channel <#channel> OR cul chat_channel <#channel> ``` Set Waifu Chat channel", inline=True)
        embed.add_field(name="Remove Waifu Channel", value="```/remove_channel <#channel> OR cul remove_channel <#channel>  ``` Remove Waifu Chat channel", inline=True)
        embed.add_field(name="Invite Command", value="```/invite OR cul invite ``` Invite Bot", inline=True)
        

        await ctx.respond(embed = helpEmbed)

    @bridge.bridge_command()
    async def invite(self,ctx):
        embed=discord.Embed(title="INVITE CUL BOT", url="https://bit.ly/3vTYyUw")
        await ctx.respond(embed=embed)



    


def setup(client):
    client.add_cog(mycommands(client))