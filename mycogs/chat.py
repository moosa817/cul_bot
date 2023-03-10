from discord.ext import commands
import config
from pymongo import MongoClient
from discord import Webhook
import asyncio
import aiohttp

client = MongoClient(config.mongo_str)
db = client.get_database('cul_bot')
records = db.server_info
                

class chat(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            if len(message.attachments) > 0 or message.embeds != []:
                await message.delete()
                return
            return
        server_id = message.guild.id
        channel_id = message.channel.id

        result = records.find_one({"id":str(server_id)})

        if not result:
            records.insert_one({"name":str(message.guild.name),"id":str(server_id),"webhook_link":"","channel_id":""})
            return
        
        if result["channel_id"] == str(channel_id):
            if len(message.attachments) > 0 or message.embeds != []:

                await message.channel.send("Hey you can't upload attachments or embeds in here its a chat only channel do /remove_channel to remove it",reference=message,delete_after=5)
                await message.delete()

                return
            
            WEBHOOK_URL = result["webhook_link"]
            MESSAGE_CONTENT = message.content
            PROFILE_PICTURE_URL = 'https://media.discordapp.net/attachments/868218686366949416/1083870739511377951/image.png'

            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(WEBHOOK_URL,session=session) # Initializing webhook

                await webhook.send(content=MESSAGE_CONTENT, username='Waifu', avatar_url=PROFILE_PICTURE_URL)
        else:
            pass
            return

        


def setup(client):
    client.add_cog(chat(client))