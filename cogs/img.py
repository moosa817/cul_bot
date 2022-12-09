import discord
from discord.ext import commands
import random
import mysql.connector
import config
# <33
conn = mysql.connector.connect(
        host=config.db_host,
        user=config.db_user,
        passwd=config.db_pwd,
        database=config.db_database)
cur = conn.cursor()

class img(commands.Cog):
    def __init__(self,client):
        
        self.client = client


    @commands.Cog.listener()
    async def on_message(self,message):
        result = cur.execute("SELECT * FROM `img_stuff`")
        results = cur.fetchall()
        names = []
        imgs = []
        og_image = ""
        for i in results:
            names.append(i[1])
            imgs.append(i[2])

        for name in names:
            if message.content.startswith(name) or message.content.startswith(name.upper()) or message.content.startswith(name.lower()) or message.content.startswith(name.capitalize()):
                index = names.index(name)
                image = imgs[index]

                print("here")
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
                    await message.channel.send(config.host+og_image)
                else:
                    await message.channel.send(og_image)
                
           

async def setup(client):
    await client.add_cog(img(client))