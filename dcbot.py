import discord 
from discord.ext import commands
import time


api = str(os.environ.get("RIOT_KEY"))


bot = commands.Bot(command_prefix ='#')

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if(message.startswith("!@#test"):
        await bot.send_message(bot.get_channel('360089608685355011'),"on")
    
    
@bot.event
async def on_member_join(member):
    name = member.name
    if(name.find("discord.gg/") >-1):
        print("contains")
        await bot.ban(member,delete_message_days=6)
        time.sleep(2)
        await bot.purge_from(bot.get_channel('360089937611325441'), limit=2)
        await bot.send_message(bot.get_channel('360089937611325441'), "Spoko prioteli nqkav random gei iskashe da reklamira server no az vi protectnah ot tozi gei")



@bot.event
async def on_ready():
    print("logged in as")
    print(bot.user.name)



bot.run(str(os.environ.get("TOKEN"))
