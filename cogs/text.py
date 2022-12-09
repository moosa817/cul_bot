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

class text(commands.Cog):
    def __init__(self,client):
        
        self.client = client


    @commands.Cog.listener()
    async def on_message(self,message):
        result = cur.execute("SELECT * FROM `text_stuff`")
        results = cur.fetchall()
        names = []
        txts = []
        for i in results:
            names.append(i[1])
            txts.append(i[2])

        for name in names:
            if message.content.startswith(name) or message.content.startswith(name.upper()) or message.content.startswith(name.lower()) or message.content.startswith(name.capitalize()):
                index = names.index(name)
                txt = txts[index]

                print("here")
                await message.channel.send(txt)                
           

async def setup(client):
    await client.add_cog(text(client))