import discord
from discord.ext import commands
import random 
import requests
import pprint


client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('Bot is Online.')

@client.command()
#this command will tell us the ping of the bot called with ".ping"
async def ping(ctx):
    title = f'pong! (Ping ms: {round(client.latency * 1000)}ms )'
    message = 'Im hosted off a rasberry pi in the middle of nowhere. Sorry if Im slow :( '
    embed = discord.Embed(
    title = title,
    description = message,
    color = discord.Color.orange()
    )
    await ctx.send(embed=embed)
    


@client.command()
async def brew(ctx,*,userInput):
        title = ''
        message = ''
        i=0 
        r = requests.get(f'https://api.openbrewerydb.org/breweries?by_postal={userInput}')
        if(len(r.json()) > 0):
            title = f"***brewBot Found {len(r.json())} results for postal code: {userInput}***"
            while (i < len(r.json())):
                message = message + f"**Brewery:** {r.json()[i]['name']}\nStreet Adress: {r.json()[i]['street']}\n"
                i = i+1
        else:
            r = requests.get(f'https://api.openbrewerydb.org/breweries?by_state={userInput}')
            if(len(r.json()) > 0):
                title = f"***brewBot Found {len(r.json())} results for the State: {userInput}***"
                while (i < len(r.json())):
                    message = message + f"**Brewery:** {r.json()[i]['name']}\nStreet Adress: {r.json()[i]['street']}\n"
                    i = i+1
            else:
                r = requests.get(f'https://api.openbrewerydb.org/breweries?by_city={userInput}')
                if(len(r.json()) > 0):
                    title = f"***brewBot Found {len(r.json())} results for the City: {userInput}***"
                    while (i < len(r.json())):
                        message = message + f"**Brewery:** {r.json()[i]['name']}\nStreet Adress: {r.json()[i]['street']}\n"
                        i = i+1
        if(i == 0):
            title = f"Sorry! I could not find anything. :(\nYou can give me a state, city, or zipcode and I will look for you. \nJust make sure it's spelled correctly!"
       
            

        embed = discord.Embed(
        title = title,
        description = message,
        color = discord.Color.orange()
        )
        await ctx.send(embed=embed)



client.run('Token here')    


"""
@client.command()
async def displayembed(ctx):
    description1 = "DESCRIPTION 1"
    description2 = "DESCRIPTION 2"
    desCat = description1 + description2
    embed = discord.Embed(
        title = 'Title',
        description = desCat,
        color = discord.Color.blue()
    )
   
    embed.set_footer(text='This is a footer.')
    #embed.set_image()
    #embed.set_thumbnail()
    #embed.set_author()
    #embed.add_field(name = "ID", value = member.id, inline= True)
    await ctx.send(embed=embed)


"""



        





