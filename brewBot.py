import discord
from discord.ext import commands
import random 
import requests
import pprint


client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()

async def brew(ctx,*,userInput):
    i=0 
    r = requests.get(f'https://api.openbrewerydb.org/breweries?by_postal={userInput}')
    if(len(r.json()) > 0):
        await ctx.send(f"***brewBot Found {len(r.json())} results for postal code: {userInput}***")
        while (i < len(r.json())):
            await ctx.send(f"**Brewery:** {r.json()[i]['name']}\nStreet Adress: {r.json()[i]['street']}\n")
            i = i+1
    else:
        r = requests.get(f'***https://api.openbrewerydb.org/breweries?by_state={userInput}***')
        if(len(r.json()) > 0):
            await ctx.send(f"brewBot Found {len(r.json())} results for the State: {userInput}")
            while (i < len(r.json())):
                await ctx.send(f"**Brewery:** {r.json()[i]['name']}\nStreet Adress: {r.json()[i]['street']}\n")
                i = i+1
        else:
            r = requests.get(f'***https://api.openbrewerydb.org/breweries?by_city={userInput}***')
            if(len(r.json()) > 0):
                await ctx.send(f"brewBot Found {len(r.json())} results for the City: {userInput}")
                while (i < len(r.json())):
                    await ctx.send(f"**Brewery:** {r.json()[i]['name']}\nStreet Adress: {r.json()[i]['street']}\n")
                    i = i+1




client.run('YOUR CER HERE') 
