from discord.ext import commands,bridge
from additional_files import google_search


# <33
class search(commands.Cog):

    def __init__(self,client):
        self.client = client


    @bridge.bridge_command(description="Search Images With Google ILLEGALLY")
    async def search(self,ctx,keyword:str,no_of_images:int=4):
        await ctx.respond("Plz Wait Fetching Images ...")

        url_list = google_search.download_images(keyword,no_of_images)
        if not url_list:
            await ctx.edit("No Images Found :()")
            return 
        if len(url_list) >= 10:
            url_list = url_list[:10]
        
        a = 0
        for i in url_list:
            if a == 0:
                await ctx.edit(content=f"{keyword}  {i}")
                a = a+1
            else:
                await ctx.send(i)
        url_list = []


def setup(client):
    client.add_cog(search(client))