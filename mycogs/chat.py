from discord.ext import commands
import config
from pymongo import MongoClient
from discord import Webhook
import aiohttp
import json

BOT_NAME = 'Waifu' 
SITUATION = 'Waifu talks to you'
X_RAPIDAPI_KEY = "4b1d765b96msh163b83ada64ba48p150ed4jsn7b12f2017f94" 
TRANSLATE_FROM = 'en' 
TRANSLATE_TO = 'en' 



client = MongoClient(config.mongo_str)
db = client.get_database('cul_bot')
records = db.server_info


async def waifu_ai_query(query, user_id, user_name):
    url = "https://waifu.p.rapidapi.com/path"

    querystring = {
        "user_id": user_id,
        "message": query,
        "from_name": user_name, 
        "to_name" : BOT_NAME,
        "situation": SITUATION,
        "translate_from": TRANSLATE_FROM,
        "translate_to": TRANSLATE_TO
    }
    
    my_obj = {
        "key1": "value",
        "key2": "value"
    }
    
    payload = json.dumps(my_obj)

    headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "waifu.p.rapidapi.com",
    'x-rapidapi-key': X_RAPIDAPI_KEY
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=headers, params=querystring) as response:
            reply = await response.text(
                encoding='utf-8'
            )

    return reply

          

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
                query = message.content
                response = await waifu_ai_query(query, message.author.id, message.author.name)

                await webhook.send(content=response, username='Waifu', avatar_url=PROFILE_PICTURE_URL)
        else:
            pass
            return

        


def setup(client):
    client.add_cog(chat(client))