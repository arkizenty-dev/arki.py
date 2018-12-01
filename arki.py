# imports modules used
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import BadArgument
from discord.ext.commands import CommandInvokeError
from discord.ext.commands import NotOwner
import platform
import time



# Variables
start_time=time.asctime()
bot = commands.Bot(command_prefix='$')
bot.remove_command('help')



# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    if isinstance(error, BadArgument):
        embed = discord.Embed(title="`ERROR!`", description="", color=0x2ca1dd)
        embed.add_field(name=str(error),value="This seems to be the problem...", inline=False)
        embed.set_footer(text="Made with ❤ by arkizenty#7140")
        await ctx.send(embed=embed)
        return
    if isinstance(error, CommandInvokeError):
        embed = discord.Embed(title="`ERROR!`", description="", color=0x2ca1dd)
        embed.add_field(name=str(error),value="This seems to be the problem...", inline=False)
        embed.add_field(name="Tip:", value="Have you tried re-inviting it? https://discordapp.com/oauth2/authorize?client_id=484539869922590721&permissions=67500096&scope=bot")
        embed.set_footer(text="Made with ❤ by arkizenty#7140")
        await ctx.send(embed=embed)
        return
    if isinstance(error, NotOwner):
        embed = discord.Embed(title="`ERROR!`", description="", color=0x2ca1dd)
        embed.add_field(name=str(error),value="This seems to be the problem...", inline=False)
        embed.set_footer(text="Made with ❤ by arkizenty#7140")
        await ctx.send(embed=embed)
        return
    raise error



# Main boot up of arki.py
@bot.event
async def on_ready():
    print(f"Now running as {bot.user.name} since {start_time} | Python Version: {platform.python_version()}")
    await bot.change_presence(activity=discord.Activity(name='Youtube', type=discord.ActivityType.watching))



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
    async def help(ctx, *, page = None):
        if page == None:
            embed = discord.Embed(title="arki.py's Command Guide™ (1/2)", description="", color=0x2ca1dd)
            embed.add_field(name=f"{bot.command_prefix}ping", value="Pong!", inline=False)
            embed.add_field(name=f"{bot.command_prefix}pong", value="Ping!", inline=False)
            embed.add_field(name=f"{bot.command_prefix}help", value="Shows a list of commands", inline=False)
            embed.add_field(name=f"{bot.command_prefix}arki.py", value="Shows info about arki.py", inline=False)
            embed.add_field(name=f"{bot.command_prefix}clock", value="Shows the date and time", inline=False)
            embed.set_footer(text="Made with ❤ by arkizenty#7140")
            await ctx.send(embed=embed)
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")
        if page == "1":
            embed = discord.Embed(title="arki.py's Command Guide™ (1/2)", description="", color=0x2ca1dd)
            embed.add_field(name=f"{bot.command_prefix}ping", value = "Pong!", inline = False)
            embed.add_field(name=f"{bot.command_prefix}pong", value = "Ping!", inline = False)
            embed.add_field(name=f"{bot.command_prefix}help", value = "Shows a list of commands", inline = False)
            embed.add_field(name=f"{bot.command_prefix}arki.py", value = "Shows info about arki.py", inline = False)
            embed.add_field(name=f"{bot.command_prefix}clock", value = "Shows the date and time", inline = False)
            embed.set_footer(text="Made with ❤ by arkizenty#7140")
            await ctx.send(embed=embed)
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")
        if page == "2":
            embed = discord.Embed(title="arki.py's Command Guide™ (2/2)", description="", color=0x2ca1dd)
            embed.add_field(name=f"{bot.command_prefix}user [User ID/Username/Nickname/Mention]", value="displays info about about a user", inline=False)
            embed.add_field(name=f"{bot.command_prefix}avatar [User ID/Username/Nickname/Mention]", value="grabs the users avatar", inline=False)
            embed.add_field(name=f"{bot.command_prefix}contribute", value="displays info about helping out with arki.py", inline=False)
            embed.set_footer(text="Made with ❤ by arkizenty#7140")
            await ctx.send(embed=embed)
            print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #info
    @bot.command()
    async def info(ctx):
        embed=discord.Embed(title="arki.py", url="https://arkizenty.github.io/arki.py/", color=0x2ca1dd)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/arkizenty/arki.py/master/Festive%20Whale.png")
        embed.add_field(name="Version", value="3.0 Rewritten", inline=False)
        embed.add_field(name="Python Version", value=platform.python_version(), inline=False)
        embed.add_field(name="Prefix", value=bot.command_prefix, inline=False)
        embed.add_field(name="Main Website", value="https://arkizenty.github.io/arki.py/", inline=False)
        embed.set_footer(text="Made with ❤ by arkizenty#7140")
        await ctx.send(embed=embed)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #clock
    @bot.command()
    async def clock(ctx):
        embed=discord.Embed(title="arki.py's Clock", color=0x2ca1dd)
        embed.add_field(name="My clock says it's currently:", value=start_time, inline=False)
        embed.set_footer(text="Made with ❤ by arkizenty#7140")
        await ctx.send(embed=embed)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #user
    @bot.command()
    async def user(ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        embed = discord.Embed(title=f"**{user.name}'s info**", color=0x2ca1dd)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="**Username:**", value=user, inline=False)
        embed.add_field(name="**Current nick:**", value=user.nick, inline=False)
        embed.add_field(name="**Status:**", value=user.status, inline=False)
        embed.add_field(name="**Bot:**", value=user.bot, inline=False)
        embed.add_field(name="**Creation Date:**", value=user.created_at, inline=False)
        embed.add_field(name="**User ID:**", value =user.id, inline=True)
        embed.set_footer(text="Made with ❤ by arkizenty#7140")
        await ctx.send(embed=embed)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #avatar
    @bot.command()
    async def avatar(ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        embed = discord.Embed(title="Here is " + user.name + "'s avatar!", url=user.avatar_url,color=0x2ca1dd)
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text="Made with ❤ by arkizenty#7140")
        await ctx.send(embed=embed)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #contribute
    @bot.command()
    async def contribute(ctx):
        await ctx.send("You can help contribute here: https://github.com/arkizenty/arki.py")
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #relax
    @bot.command()
    async def relax(ctx):
        await ctx.send(f"come chill out and Ｒ　ｅ　Ｌ　ａ　ｘ　  with this video {ctx.author.mention} https://youtu.be/WYUOKnZkgko")
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #pour
    @bot.command()
    async def pour(ctx):
        await ctx.send("Just pouring some water... https://youtu.be/IJ-PVdapaDU")
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #nitrobrew
    @bot.command()
    async def nitrobrew(ctx):
        await ctx.send("Some of the nicest of grinded beans around...")
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #tayne
    @bot.command()
    async def tayne(ctx):
        await ctx.send(" https://youtu.be/1vjulniffcA")
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #love
    @bot.command()
    async def love(ctx):
        await ctx.send("What is love? I never experienced 'love' before.. I'm just a bot that was built to do tasks and not love or feel...")
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



    #adding
    @bot.command()
    @commands.is_owner()
    async def add(ctx, left : int, right : int):
        await ctx.send(left + right)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #stream
    @bot.command()
    @commands.is_owner()
    async def stream(ctx, *, streaming):
        game = discord.Activity(type=discord.ActivityType.streaming,name=streaming, url="https://www.twitch.tv/arkizenty/")
        await bot.change_presence(activity=game)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #play
    @bot.command()
    @commands.is_owner()
    async def play(ctx, *, playing):
        game = discord.Activity(type=discord.ActivityType.playing,name=playing)
        await bot.change_presence(activity=game)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #watch
    @bot.command()
    @commands.is_owner()
    async def watch(ctx, *, watching):
        game = discord.Activity(type=discord.ActivityType.watching,name=watching)
        await bot.change_presence(activity=game)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #listen
    @bot.command()
    @commands.is_owner()
    async def listen(ctx, *, listening):
        game = discord.Activity(type=discord.ActivityType.listening,name=listening)
        await bot.change_presence(activity=game)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")



    #say
    @bot.command()
    @commands.is_owner()
    async def say(ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)
        print(f"{ctx.author} just used {bot.command_prefix}{ctx.command} on {start_time} | User ID: {ctx.author.id}")






# Bot token
bot.run('token?')
