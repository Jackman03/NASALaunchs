#Commands
#Program that sends the launch schedule to discord
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from GetLaunches import GetLaunches
from datetime import datetime

INTENTS = discord.Intents(messages=True, guilds=True,message_content = True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!',intents=INTENTS)

@bot.event
async def on_ready():
    print(f'bot has connected to Discord!')


#Command that lists all launches
#data to send back
#Image
#Name
#Vehicle
#Provider
#Date
#Location on map
@bot.command()
async def launches(ctx):
    print(f'Running command to get current launches')
    now = datetime.now()
    FormatedTime = now.strftime('%m/%d/%y %H:%M:%S')
    await ctx.send(f'Launches as of {FormatedTime}')
    CurrentLaunchData = GetLaunches()
    #e=launches are returned in order so we dont have to sort them.
    embedMsg = discord.Embed(title='Current Launches',
                           description='The current launches, there dates and locations',
                           color=discord.Color.blue())

    for launch in CurrentLaunchData:
        LaunchValue = f'{launch['vehicle']}\n location: {launch['location']}, Pad: {launch['pad']}\n status: {launch['status']}\n\n'
        embedMsg.add_field(name=launch['name'], value=LaunchValue, inline=False)
    await ctx.send(embed=embedMsg)

#command to find the next launch. This should normally be the 1st one in the json file.
@bot.command()
async def nextlaunch(ctx):
    print(f'running command to find the next launch.')
    #returns the first launch in the json.
    NextLaunchData = GetLaunches()[0]
    URL = NextLaunchData['vehicle_config_image']
    LauchTime = datetime.strptime(NextLaunchData['net'],'%Y-%m-%dT%H:%M:%SZ')

    embedMsg = discord.Embed(title='Next Launch',
                             description='This is the next launch',
                             color=discord.Color.gold(),
                             timestamp=LauchTime)
    
    embedMsg.set_image(url=URL)
    LaunchValue = f'{NextLaunchData['vehicle']}\n location: {NextLaunchData['location']}, Pad: {NextLaunchData['pad']}\n status: {NextLaunchData['status']}\n\n'
    embedMsg.add_field(name=NextLaunchData['name'], value=LaunchValue, inline=False)
    await ctx.send(embed=embedMsg)

    
    


#error handelinfg 
@bot.event
async def on_command_error(ctx,error):
    #if command is not found
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Sorry, I don't recognize that command. Type `!Help` for a list of available commands.")
    #other error
    else:
        await ctx.send(f"An error occured: {str(error)}")

bot.run(TOKEN)
#data to send back
#Image
#Name
#Vehicle
#Provider
#Date
#Location on map
