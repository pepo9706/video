import discord 
from discord.ext import commands
import time
import os

bot = commands.Bot(command_prefix ='#')

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    
    
    
@bot.event
async def on_member_join(member):
    name = member.name
    if(name.find("discord.gg/") >-1):
        print("contains")
        await bot.send_message(member, 'Gori v moita banq retard umrql , dano da hvanesh rak i da umresh v kalta ,pedal qj kur')
        time.sleep(1)
        await bot.ban(member,delete_message_days=6)
        print(name+" was banned")
        time.sleep(3)
        await bot.purge_from(bot.get_channel('360089937611325441'), limit=2)
        time.sleep(3)
        await bot.send_message(bot.get_channel('360089937611325441'), "Spoko prioteli nqkav random gei iskashe da reklamira server no az vi protectnah ot tozi gei")
        


@bot.event
async def on_ready():
    print("logged in as")
    print(bot.user.name)


bot.run(os.environ["TOKEN"])
