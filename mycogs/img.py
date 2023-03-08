from discord.ext import commands
import random
from pymongo import MongoClient

import config
# <33
client = MongoClient(config.mongo_str)
db = client.get_database('cul_bot')
records = db.img_stuff
                

class img(commands.Cog):
    def __init__(self,client):
        
        self.client = client


    @commands.Cog.listener()
    async def on_message(self,message):
        result = records.find({})
        

        names = []
        imgs = []
        og_image = ""
        for i in result:
            names.append(i.get("name"))
            imgs.append(i.get("img"))

        for name in names:
            if message.content.startswith(name) or message.content.startswith(name.upper()) or message.content.startswith(name.lower()) or message.content.startswith(name.capitalize()):
                index = names.index(name)
                image = imgs[index]

                # print("here")
                images = []
                for k in image.split(","):
                    images.append(k)

                
                og_image = random.choice(images)
                try:
                    a,b,c = og_image.split("/")
                    if a == "static":
                        is_img = True
                except:
                    is_img = False
                
                if is_img:
                    await message.channel.send(config.host+og_image,reference=message)
                else:
                    await message.channel.send(og_image,reference=message)
                
           

def setup(client):
    client.add_cog(img(client))