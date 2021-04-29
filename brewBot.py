import discord
from discord.ext import commands
import random 
import requests
import pprint

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()

async def beer(ctx,*,zipcode):
    r = requests.get(f'https://api.openbrewerydb.org/breweries?by_postal={zipcode}')
    i = 0
    if(len(r.json()) == 0):
        await ctx.send("ERROR: No breweries found make sure postal code is right")
    while (i < len(r.json())):
        await ctx.send(f"Brewery: {r.json()[i]['name']}")
        await ctx.send(f"Street Adress: {r.json()[i]['street']}")
        await ctx.send(f"Website: {r.json()[i]['website_url']}")
        i = i+1
 

client.run('BOT_TOKEN_HERE') 