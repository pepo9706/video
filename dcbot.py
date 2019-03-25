import discord 
from discord.ext import commands
import time
import os

bot = commands.Bot(command_prefix ='#')

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if "discord.gg/" in message.content:
        await bot.purge_from(bot.get_channel('323779754513924106'), limit=1)
        time.sleep(1)
        await bot.send_message(message.channel, message.author+" shte te vkaram v banq :) laino")
    
    
    
@bot.event
async def on_member_join(member):
    name = member.name
    if(name.find("discord.gg/") >-1 or name.find("twitter.com/") >-1 or name.find("twitch.tv/") >-1 or name.find("discord.me/") > -1):
        print("contains")
        await bot.send_message(member, 'Gori v moita banq retard umrql , dano da hvanesh rak i da umresh v kalta ,pedal qj kur')
        time.sleep(1)
        await bot.ban(member,delete_message_days=6)
        print(name+" was banned")
        time.sleep(3)
        await bot.purge_from(bot.get_channel('323785237639200769'), limit=2)
        time.sleep(3)
        await bot.send_message(bot.get_channel('323785237639200769'), "Spoko prioteli nqkav random gei iskashe da reklamira server no az vi protectnah ot tozi gei")
        


@bot.event
async def on_ready():
    print("logged in as")
    print(bot.user.name)


bot.run(os.environ["TOKEN"])
