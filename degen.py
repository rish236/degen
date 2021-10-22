import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
import pandas as pd
from discord import utils
import random as r
import time
from discord.ext.commands import has_permissions


TOKEN = os.environ['degen_token']

bot = commands.Bot(command_prefix='!')

bot.counter = 0


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='pray', help = '')
async def check(member):
    author = member.author.name
    discord_tag = member.author.discriminator
    discord_id = member.author.id
    discord_username = author + "#" + discord_tag
    f = open('names.txt','a')

    df = pd.read_csv("removed_dups.csv")

    try:
        roles = member.guild.roles
    except Exception as e:
        print(e)
        time.sleep(.3)


    try:
        purgatory_role = discord.utils.get(roles, name="Purgatory")
    except Exception as e:
        purgatory_role = discord.utils.get(member.guild.roles, name="Purgatory")


    print(purgatory_role)
    blessed_role = discord.utils.get(member.guild.roles, name="Blessed by 2AC")
    blessed_chance = r.randint(0,3000)
    print(f"{member.author}: {blessed_chance}")
   
    try:
        if str(member.author) in df["whitelist"].valsues or blessed_chance == 69:
            await member.author.add_roles(blessed_role)
            if blessed_chance == 69:
                await member.send(embed=discord.Embed(title="A message from 2AC:", description=f"{member.author.mention}, you have been chosen out of 5,000 people to be blessed. 👼👼", color = 0))
                f.write(discord_username + " whitelist 69 \n")
            
            else:
                await member.send(embed=discord.Embed(title="A message from 2AC:", description=f"{member.author.mention}, you have been blessed. 👼👼", color = 0))
                f.write(discord_username + " whitelist\n")
                return
        else:
            print("got here blacklist")
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

@bot.command(name="ban",pass_context=True)
@has_permissions(administrator=True)
async def ban_everyone(ctx):
    for member in ctx.guild.members:
        if len(member.roles) < 2:
            print(member)
            await ctx.send(member)

   
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