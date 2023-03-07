from discord.ext import commands,bridge
from additional_files import pint_api

pint_scrapper = pint_api.PinterestImageScraper()

# <33
class search(commands.Cog):

    def __init__(self,client):
        self.client = client


    @bridge.bridge_command(description="Search Images With Pinterest")
    async def search(self,ctx,keyword:str,no_of_images:int=4):
        msg = await ctx.respond("Plz Wait Fetching Images ...")
        url_list = pint_scrapper.make_ready(keyword)
        if len(url_list) >= 10:
            url_list = url_list[:10]
        
        url_list = url_list[:no_of_images]
        a = 0
        for i in url_list:
            if a == 0:
                await ctx.edit(content=f"{keyword}  {i}")
                a = a+1
            else:
                await ctx.send(i)


def setup(client):
    client.add_cog(search(client))