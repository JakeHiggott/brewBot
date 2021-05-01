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

@client.command()
async def info(ctx,*,userInput):
    title = ''
    message = ''
    i=0 
    r = requests.get(f'https://api.openbrewerydb.org/breweries/search?query={userInput}')
    if(len(r.json()) > 25):
            title = f"***brewBot Found {len(r.json())} results for search request: {userInput}\nOnly showing the top 25 results***"
            while (i < len(r.json()) and i <= 20):
                message = message + f"**Brewery:** {r.json()[i]['name']}     (**ID: **{r.json()[i]['id']})\nStreet Adress: {r.json()[i]['street']}\n"
                i = i+1
    else:
        if(len(r.json()) > 0 and len(r.json()) < 25):
            title = f"***brewBot Found {len(r.json())} results for search request: {userInput}***"
            while (i < len(r.json())):
                message = message + f"**Brewery:** {r.json()[i]['name']}     (**ID: **{r.json()[i]['id']})\nStreet Adress: {r.json()[i]['street']}\n"
                i = i+1           
        else:
            title = f"Sorry! I could not find anything. :(\nMake sure it's spelled correctly!"
    embed = discord.Embed(
    title = title,
    description = message,
    color = discord.Color.orange()
    )
    await ctx.send(embed=embed)

@client.command()
async def introduce(ctx):
    
    embed = discord.Embed(
        title = f'Hi I am Brew Bot!',
        description = f'If you would like to know more about my different commands call the **!help** command or checkout my documentation!(https://github.com/JakeHiggott/brewBot) \n If you want to help build me let https://github.com/JakeHiggott know! I acess the Open Brewery DB API check them out! ',
        color = discord.Color.blue()
    )
   
    embed.set_footer(text='https://github.com/openbrewerydb')
    embed.set_image(url = "https://raw.githubusercontent.com/openbrewerydb/openbrewerydb-gatsby/master/content/images/obdb-hacktoberfest-2020-banner.png")
    #embed.set_thumbnail()
    #embed.set_author()
    #embed.add_field(name = "ID", value = member.id, inline= True)
    await ctx.send(embed=embed)







client.run('token')    







        





