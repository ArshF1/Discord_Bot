import discord
import google.generativeai as genai
import os
from dotenv import load_dotenv
from time import sleep
import array as arr

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel("gemini-pro")

intents=discord.Intents.all()
intents.members=True
client=discord.Client(intents=intents)

serverAdmin=arr.array("q",[741931775835635764])
userAdmin=arr.array("q",[741931775835635764])

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
@client.event
async def on_message(message):
    if message.author==client.user:
        return
    elif message.content.startswith("-Hello"):
        await message.channel.send("Hello")
    elif message.content=="-a":
        await message.channel.send(message.author.mention+" Bot is working!")
    elif message.content.startswith("-add"):
        userAdmin.append(int(message.content[7:len(message.content)-1].strip()))
        await message.channel.send(message.content[4:len(message.content)].strip()+" is now an admin!")
    elif message.content=="-list server" and message.author.id in serverAdmin:
        for server_names in client.guilds:
            await message.channel.send(server_names)
    elif message.content.lower().startswith("aria"):
        response=model.generate_content(message.content[5:].strip())
        # await message.channel.send("Hello user")
        await message.channel.send(f"{message.author.mention} {response.text}")
    elif message.content=="-members":
            # print(message.channel.mention)
            # print(type(message.channel.mention))
            # print(message.author.name)
            # for guild in client.guilds:
            #     print(guild.name, guild.id)
        for guild in client.guilds:
            if guild.id==message.guild.id:
                for member in guild.members:
                    await message.channel.send(member)
                break
    elif message.content=="-tagall":
        for guild in client.guilds:
            if guild.id==message.guild.id:
                for member in guild.members:
                    if member._user==client.user:
                        # print(member._user, client.user)
                        pass
                    else:
                        await message.channel.send(member.mention)
    elif message.content=="-exit" and message.author.id in serverAdmin:
        await message.channel.send("Shutting Down Aria.......")
        sleep(1)
        await message.channel.send("Have a nice day! ")
        exit()
    else:
        if message.content.startswith("-"):
            await message.channel.send("Incomplete Command 🙂")
        else:
            pass
            await message.channel.send("Kya matlab tumhare liye command nahi hai 🤭🤭")

# @client.event
# async def on_message(message):
#     command=str(message.content.lower().startswith())
#     # print(message.content)
#     match command:
#         case "-hello":
#             await message.channel.send("Hello "+message.author.mention)
#         case "-a":
#             await message.channel.send(message.author.mention+ " Bot is working!")
#         case "-list server":
#             if message.author.id in serverAdmin:
#                 for server_names in client.guilds:
#                     await message.channel.send(server_names)
#         case "":
#             response=model.generate_content(message.content[5:].strip())
#             await message.channel.send(f"{message.author.mention} {response.text}")
        

token=os.getenv("DISCORD_TOKEN")
client.run(token=token)
