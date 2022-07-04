# import discord
# from discord.ext import commands
# import time
# import os
# import random

# # <33
# class cul(commands.Cog):
#     def __init__(self,client):
#         self.client = client

#     @commands.Cog.listener()
#     async def on_ready(self):
#         print("ADDED cul.py cul")

#     @commands.Cog.listener()
#     async def on_message(self,message):
#         pass
#         if message.content.startswith('cool') or message.content.startswith('kul') or message.content.startswith('kewl'):
#             await message.delete()
#             # await message.channel.send(f"cul from: @{message.author}")


#             e = discord.Embed(title="cul",description=f"from {message.author.mention}")
#             await message.channel.send(embed=e)
#             # await message.channel.send("cul")
#         #     e = os.getcwd()
#         #     files = os.listdir(e+"/data/loml")
            
#         #     random.shuffle(files)
#         #     gg = e+'/data/loml/'+files[0]

#         #     await message.channel.send(file=discord.File(gg))




# def setup(client):
#     client.add_cog(cul(client))
