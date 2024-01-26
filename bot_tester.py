import os
from dotenv import load_dotenv
import discord
import google.generativeai as genai
from time import sleep

load_dotenv()

intents=discord.Intents.all()
intents.members=True
client=discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print([guild.name for guild in client.guilds])

@client.event
async def on_message(message):
    # print(message.guild.mention)
    if message.author==client.user:
        return
    else:
        print("Author: "+str(message.author))
        print(message.content)
        print(message.author, message.author.id)
        # print(str(message.author)=="arsh_sahay")
        print(message.author.mention)
        print("\n")
    

token=os.getenv("DISCORD_TOKEN")
client.run(token=token)