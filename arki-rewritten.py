# imports modules used

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import platform
import time
import random



# Variables

python_version=platform.python_version()

start_time=time.asctime()

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')



# Prevents "command not found" error

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error



# Main boot up of arki.py
@bot.event
async def on_ready():
    print(f'Currently running on Python Version {python_version}')
    print(f'Now running arki.py since {start_time}!')
    await bot.change_presence(activity=discord.Game(name='Youtube', type=3))



    #Ping
    @bot.command()
    async def ping(ctx):
        await ctx.send(':ping_pong: Pong!')
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #Pong
    @bot.command()
    async def pong(ctx):
        await ctx.send(':ping_pong: Ping!')
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #help
    @bot.command()
    async def help(ctx):
        embed = discord.Embed(title="Commands:", description="", color=0x2ca1dd)
        embed.set_author(name="arki.py Command Guide™")
        embed.add_field(name=f"{bot.command_prefix}ping", value = "Pong!", inline = False)
        embed.add_field(name=f"{bot.command_prefix}pong", value = "Ping!", inline = False)
        embed.add_field(name=f"{bot.command_prefix}help", value = "Shows a list of commands", inline = False)
        embed.add_field(name=f"{bot.command_prefix}arki.py", value = "Shows info about arki.py", inline = False)
        embed.add_field(name=f"{bot.command_prefix}time", value = "Shows the date and time", inline = False)
        embed.add_field(name=f"{bot.command_prefix}user", value = "displays info about about a user", inline = False)
        embed.add_field(name=f"{bot.command_prefix}avatar", value = "grabs the mentioned users avatar", inline = False)
        embed.add_field(name=f"{bot.command_prefix}contribute", value="displays info about helping out with arki.py", inline = False)
        embed.add_field(name=f"{bot.command_prefix}credits", value="displays contributers of arki.py!", inline = False)
        embed.set_footer(text="Made with ❤ by arki#8251")
        await ctx.send(embed=embed)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #arki
        @bot.command()
        async def arki(ctx):
            embed=discord.Embed(title="arki.py", url="https://discordbots.org/bot/484539869922590721#", color=0x2ca1dd)
            embed.set_thumbnail(url="https://raw.githubusercontent.com/arkizenty/arki.py/master/arkizenty(larger).png")
            embed.add_field(name="Version", value = "1.0 Rewritten", inline = False)
            embed.add_field(name="Python Version", value = f'{python_version}', inline = False)
            embed.add_field(name="Prefix", value = f"{bot.command_prefix}", inline = False)
            embed.add_field(name="Discord Bot List", value = "https://discordbots.org/bot/484539869922590721#", inline = False)
            embed.set_footer(text="Made with ❤ by arki#8251")
            await ctx.send(embed=embed)
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #time
        @bot.command()
        async def time(ctx):
            embed=discord.Embed(title="Current time:")
            embed.add_field(name=f"{start_time}", value=undefined, inline=False)
            embed.set_footer(text="Made with ❤ by arki#8251")
            await ctx.send(embed=embed)
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #user (Currently not functional)
        @bot.command()
        async def user(ctx):
            await ctx.send("Currently not coded in yet")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #avatar (Currently not functional)
        @bot.command()
        async def avatar(ctx):
            await ctx.send("Currently not coded in yet")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #contribute
        @bot.command()
        async def contribute(ctx):
            await ctx.send("You can help contribute here: goo.gl/VwHjae")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #credits
        @bot.command()
        async def credits(ctx):
            embed = discord.Embed(title="Credits:", description="", color=0x2ca1dd)
            embed.set_author(name="arki.py Credits™")
            embed.add_field(name="arki#8251", value = "The creator of arki.py", inline = False)
            embed.add_field(name="EpicShardGamingYT#6666", value = "originaly helped prevent arki.py from responding to other bots", inline = False)
            embed.set_footer(text="Made with ❤ by arki#8251")
            await ctx.send(embed=embed)
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #relax
        @bot.command()
        async def relax(ctx):
            await ctx.send(f"Ｒ　ｅ　Ｌ　ａ　ｘ　 {ctx.author.mention} https://youtu.be/WYUOKnZkgko")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #pour
        @bot.command()
        async def pour(ctx):
            await ctx.send("https://youtu.be/IJ-PVdapaDU")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #joke
        @bot.command()
        async def joke(ctx):
            await ctx.send("wanna hear a joke? The jokes aren't even added. ha. ha. ha. oof")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #nitrobrew
        @bot.command()
        async def nitrobrew(ctx):
            await ctx.send("https://youtu.be/9Z4GW6Vd6NI")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #tayne
        @bot.command()
        async def tayne(ctx):
            await ctx.send("https://youtu.be/1vjulniffcA")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #love
        @bot.command()
        async def love(ctx):
            await ctx.send("What is love? Anyways, here is your video https://youtu.be/XAWgeLF9EVQ")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #snek
        @bot.command()
        async def snek(ctx):
            await ctx.send("https://youtu.be/z5h_vivdGss")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



        #golang
        @bot.command()
        async def golang(ctx):
            await ctx.send("Now yes, there is golang. Some *people* wanted arki to rewrite me in golang but the problem is arki just started with python, that would mean arki would have to start over. Plus arki just barely setted me up on a raspberry pi.")
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



# Bot token
bot.run('Token?')
