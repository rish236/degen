import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
import pandas as pd
from discord import utils
import random as r
import time
from discord.ext.commands import has_permissions
import pymysql


TOKEN = os.environ['degen_token']

bot = commands.Bot(command_prefix='!')

bot.counter = 0

def connect_db():
    conn = pymysql.connect(user=os.environ['degen_db_user'], password=os.environ['degen_db_password'],host=os.environ['degen_db_host'], database=os.environ['degen_db_name'])
    conn.autocommit(True)
    return conn

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='cope')
async def cope(ctx):
    print(ctx.author)

    conn = connect_db()
    with conn:
        cursor = conn.cursor()

        query = f'''SELECT cope_count from users where disc = {ctx.author} '''
        cursor.execute(query)
        cope_count = cursor.fetchall()
        print(cope_count)

        
        
        





            
            # query = f"INSERT INTO users (disc) VALUES ({_})"
            # cursor.execute(query)
    


        


@bot.command(name='pray', help = '')
async def pray(member):
    author = member.author.name
    discord_tag = member.author.discriminator
    discord_id = member.author.id
    discord_username = author + "#" + discord_tag
    f = open('names.txt','a')

    df = pd.read_csv("removed_dups.csv")


    roles = member.guild.roles
   

    purgatory_role = discord.utils.get(roles, id=899420586021896253)
    blessed_role = discord.utils.get(roles, id=899427407935713331)

    blessed_chance = r.randint(0,2000)
    print(f"{member.author}: {blessed_chance}")
   
    try:
        if str(member.author) in df["whitelist"].values or blessed_chance == 69:
            await member.author.add_roles(blessed_role)
            if blessed_chance == 69:
                await member.send(embed=discord.Embed(title="A message from 2AC:", description=f"{member.author.mention}, you have been blessed. 👼👼👼", color = 0))
                f.write(discord_username + " whitelist 69 \n")
            
            else:
                await member.send(embed=discord.Embed(title="A message from 2AC:", description=f"{member.author.mention}, you have been blessed. 👼👼", color = 0))
                f.write(discord_username + " whitelist\n")
                return
        else:
            await member.send(embed=discord.Embed(title="A message from 2AC:", description=f"{member.author.mention}, something is brewing inside you. 💀💀", color = 0))
            try:
                await member.author.add_roles(purgatory_role)
            except Exception as e:
                f.write(discord_username + "unable to add to blacklist " + e +   "\n")
                return

            f.write(discord_username + " blacklist \n")
            return

    except Exception as e:
        
        await member.send(embed=discord.Embed(title="A message from 2AC:", description=f"{member.author.mention}, something is brewing inside you. 💀💀", color = 0))
        await member.author.add_roles(purgatory_role)
        f.write(discord_username + " blacklist, exception\n")
        return


@bot.command(name="horror",pass_context=True)
async def horror(ctx):
    await ctx.send("<a:horror:900309150494490654> <a:horror:900309150494490654> <a:horror:900309150494490654> <a:horror:900309150494490654> <a:horror:900309150494490654>")


@bot.command(name="vibe",pass_context=True)
async def vibe(ctx):
    await ctx.send("<a:toadz:897914471895429120> <a:toadz:897914471895429120> <a:toadz:897914471895429120> <a:toadz:897914471895429120> <a:toadz:897914471895429120>")

    

   
@bot.command(name="appeal",pass_context=True)
async def appeal(ctx):
    author_id = ctx.author.id
    print(author_id)
    await ctx.author.create_dm()
    try:
        await ctx.author.send('Fill out the form to appeal for a blessing: https://forms.gle/QgxaaR7p7iNRf1d38')
        await ctx.send(embed=discord.Embed(title="A message from 2AC:", description="Check your pockets. 🪙🪙", color = 0))
    except Exception as e:
        await ctx.send(embed=discord.Embed(title="A message from degen:", description="Error 401: Unable to submit dm. Make sure you have direct messages from server members turned on. 🤖🤖", color = 0))
        await ctx.send(file=discord.File('open_dm.png'))


@bot.command(name="register",pass_context=True)
async def register(ctx):
    f = open('registered.txt','a')
    f.write(f"{ctx.author} : {bot.counter}\n")
    bot.counter += 1
    await ctx.send(embed=discord.Embed(title="A message from degen:", description="You have successfully registered. 🤖🤖", color = 0))




bot.run(TOKEN)