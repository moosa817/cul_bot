from discord.ext import commands,bridge
from additional_files import pint_api


# <33
class mycommands(commands.Cog):

    def __init__(self,client):
        self.client = client


    # @bridge.bridge_command(description="Solve Expressions or Equations")
    # async def calculate(self,ctx,expression:str):
    #   pass


def setup(client):
    client.add_cog(mycommands(client))