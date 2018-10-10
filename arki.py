# imports modules used

import discord
import platform
import time
import random



# Variables

python_version=platform.python_version()
start_time=time.asctime()




# a~arki quotes

quotes = ['For some reason, people started calling me a "markov-bot clone"',
          'I have started running on a raspberry pi now, but I feel a lot slower now',
          'Someday I will say something useful things, but for now I can not think of any',
          'I wonder when arkizenty is going to add anything useful...',
          'Heh, I can run 24/7 now',
          'I wonder how arkizenty is doing...',
          '$time... darn, arki fixed it already',
          'Showouts to simple flips!',
          'This is boring...',
          f'How are you doing?',
          f'update :clap: python :clap: arki']
random.shuffle(quotes)



# $jokes quotes

jokes = ["I told my wife she was drawing her eyebrows too high. She looked surprised. ```Joke created by Scrappy_Larue https://www.reddit.com/r/AskReddit/comments/2f17dv/whats_your_best_two_line_joke/ck538op```",
         "My grandpa's last words before kicking the bucket.  Grandpa: I wonder how far I can kick this bucket.. ```Joke created by ??? https://www.reddit.com/r/AskReddit/comments/3d08ds/whats_your_favourite_one_or_twoline_joke/ct0oexz```",
         "What goes down but doesn't come up?. A yo ```Joke created by goatman2112 https://www.reddit.com/r/AskReddit/comments/71ls3r/whats_a_joke_so_bad_its_good/dnboux1```",
         "What's red and brown and bad for your teeth?. A brick. ```Joke created by Shadowthief150 https://www.reddit.com/r/AskReddit/comments/71ls3r/whats_a_joke_so_bad_its_good/dnc2igd```"]
random.shuffle(jokes)




class MyClient(discord.Client):
    async def on_ready(self):
        print (f'Currently running on Python Version {python_version}')
        print(f'Now running arki.py since {start_time}!'.format(self.user))
        await client.change_presence(game=discord.Game(name= 'Youtube', type=3))

        @client.event
        async def on_message(message):
            if message.author.bot: return



            # Regular Commands

            if message.content.lower() == "$ping":
                await client.send_message(message.channel, ':ping_pong: Pong!')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $ping on {start_time} | user id: {message.author.id}')



            if message.content.lower() == "$pong":
                await client.send_message(message.channel, ':ping_pong: Ping!')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $pong on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$help'):
                embed = discord.Embed(title="Commands:", description="", color=0x2ca1dd)
                embed.set_author(name="arki.py Command Guide™")
                embed.add_field(name="$ping", value = "Pong!", inline = False)
                embed.add_field(name="$pong", value = "Ping!", inline = False)
                embed.add_field(name="$help", value = "Shows a list of commands", inline = False)
                embed.add_field(name="$arki.py", value = "Shows info about arki.py", inline = False)
                embed.add_field(name="$time", value = "Shows the date and time", inline = False)
                embed.add_field(name="$secret", value = "Shows the secret commands (Via Direct Messages)", inline = False)
                embed.add_field(name="$user", value = "displays info about about a user", inline = False)
                embed.add_field(name="$avatar", value = "grabs the mentioned users avatar", inline = False)
                embed.add_field(name="$contribute", value="displays info about helping out with arki.py", inline = False)
                embed.add_field(name="$credits", value="displays contributers of arki.py!", inline = False)
                embed.set_footer(text="Made with ❤ by arki#8251")
                await client.send_message(message.channel, embed=embed)
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $help on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$secret'):
                embed = discord.Embed(title="Secret Commands:", color=0x2ca1dd)
                embed.set_author(name="arki's Super Secret Commands Guide")
                embed.add_field(name="$relax", value ="???", inline = False)
                embed.add_field(name="$pour", value ="???", inline = False)
                embed.add_field(name= "@someone", value ="???", inline = False)
                embed.add_field(name="a~arki", value ="???", inline = False)
                embed.add_field(name="$joke", value ="???", inline = False)
                embed.add_field(name="$nitrobrew", value ="???", inline = False)
                embed.add_field(name="$tayne", value ="???", inline = False)
                embed.add_field(name="$love", value ="???", inline = False)
                embed.add_field(name="$snek", value ="???", inline = False)
                embed.add_field(name="$1980s", value ="???", inline = False)
                embed.add_field(name="$golang", value ="???", inline = False)
                embed.set_footer(text="Made with ❤ by arki#8251")
                await client.send_message(message.author, embed=embed)
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $secrets on {start_time} | user id: {message.author.id}')



            if message.content.lower() == "$arki.py":
                embed=discord.Embed(title="arki.py", url="https://discordbots.org/bot/484539869922590721#", color=0x2ca1dd)
                embed.set_thumbnail(url="https://raw.githubusercontent.com/arkizenty/arki.py/master/arkizenty(larger).png")
                embed.add_field(name="Version", value = "2.0", inline = False)
                embed.add_field(name="Python Version", value = f'{python_version}', inline = False)
                embed.add_field(name="Prefix", value = "$", inline = False)
                embed.add_field(name="Discord Bot List", value = "https://discordbots.org/bot/484539869922590721#", inline = False)
                embed.set_footer(text="Made with ❤ by arki#8251")
                await client.send_message(message.channel, embed=embed)
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $arki.py on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$time'):
                await client.send_message(message.channel, f'```Currently {start_time}```')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $time on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith ("$contribute"):
                await client.send_message(message.channel, 'Come help out with arki.py and we can both jam in peace https://youtu.be/SHvhps47Lmc ```Github: goo.gl/VwHjae```')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $contribute on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$user'):
                message.content.split(" ")
                "%s" % (message.mentions.__len__()>0)

                for user in message.mentions:

                    embed = discord.Embed(title=f"{user.name}'s info", color=0x2ca1dd)
                    embed.set_thumbnail(url=f"{user.avatar_url}")
                    embed.add_field(name="Username:", value = f"{user}", inline = False)
                    embed.add_field(name="Current nick:", value = f"{user.nick}", inline = False)
                    embed.add_field(name="Status:", value = f"{user.status}", inline = False)
                    embed.add_field(name="Bot:", value = f"{user.bot}", inline = False)
                    embed.add_field(name="Creation Date:", value = f"{user.created_at}", inline = False)
                    embed.add_field(name="User ID:", value = f"{user.id}", inline = True)
                    embed.set_footer(text="Made with ❤ by arki#8251")
                    await client.send_message(message.channel, embed=embed)
                    print(f'{message.author} used $user on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$avatar'):
                message.content.split(" ")
                "%s" % (message.mentions.__len__() > 0)

                for user in message.mentions:
                    embed = discord.Embed(title=f"Here is {user.name}'s avatar!", url=f"{user.avatar_url}",color=0x2ca1dd)
                    embed.set_image(url=f"{user.avatar_url}")
                    embed.set_footer(text="Made with ❤ by arki#8251")
                    await client.send_message(message.channel, embed=embed)
                    await client.add_reaction(message, emoji="✅")
                    print(f'{message.author} used $avatar on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$credits'):
                embed = discord.Embed(title="Credits:", description="", color=0x2ca1dd)
                embed.set_author(name="arki.py Credits™")
                embed.add_field(name="arki#8251", value = "The creator of arki.py", inline = False)
                embed.add_field(name="EpicShardGamingYT#6666", value = "Helped prevent arki.py from responding to other bots", inline = False)
                embed.set_footer(text="Made with ❤ by arki#8251")
                await client.send_message(message.channel, embed=embed)
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $help on {start_time} | user id: {message.author.id}')



            # Secret Commands

            if message.content.lower().startswith('$relax'):
                await client.send_message(message.channel, f'Ｒ　ｅ　Ｌ　ａ　ｘ　 {message.author.mention} https://youtu.be/WYUOKnZkgko')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $relax on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$pour'):
                await client.send_message(message.channel, 'https://youtu.be/IJ-PVdapaDU')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $pour on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('@someone'):
                await client.send_message(message.channel, 'https://youtu.be/BeG5FqTpl9U')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used @someone on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('a~arki'):
                await client.send_message(message.channel, random.choice(quotes))
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used a~arki on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$joke'):
                await client.send_message(message.channel, random.choice(jokes))
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $joke on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$nitrobrew'):
                await client.send_message(message.channel, 'https://youtu.be/9Z4GW6Vd6NI')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $nitrobrew on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$tayne'):
                await client.send_message(message.channel, 'https://youtu.be/1vjulniffcA')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $tayne on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$love'):
                await client.send_message(message.channel, 'What is love? Anyways, here is your video https://youtu.be/XAWgeLF9EVQ')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $love on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$snek'):
                await client.send_message(message.channel, 'https://youtu.be/z5h_vivdGss')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $snek on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$1980s'):
                await client.send_message(message.channel, 'https://youtu.be/2UgPAZtRErI')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $1980s on {start_time} | user id: {message.author.id}')



            if message.content.lower().startswith('$golang'):
                await client.send_message(message.channel, 'Now yes, there is golang. Some *people* wanted arki to rewrite me in golang but the problem is arki just started with python, that would mean arki would have to start over. Plus arki just barely setted me up on a raspberry pi.')
                await client.add_reaction(message, emoji="✅")
                print(f'{message.author} used $1980s on {start_time} | user id: {message.author.id}')





            # Filters

            if message.content.lower().startswith('suicide'):
                await client.send_message(message.author, 'Oh hi, is everything alright? If you feel like giving up, please dont! You got so much more in life! Please call this number if you feel like giving up, if you dont have a phone then please go to this website ```Suicide Prevention Number: 1-800-273-8255``` ```Suicide Prevention Site: https://suicidepreventionlifeline.org/```')
                print(f'{message.author} said suicide on {start_time} [ATTENTION] | user id: {message.author.id}')



            # Bot Dev Commands

            if  message.content.lower().startswith('$dev'):
                if message.author.id == "420777499627094036":

                    embed = discord.Embed(title="Dev Commands:", description="", color=0x2ca1dd)
                    embed.set_author(name="arki.py Dev Commands Guide™")
                    embed.add_field(name="$say", value="Repeats the same words as you do", inline=False)
                    embed.add_field(name="$play", value="Change what the bot is playing", inline=False)
                    embed.add_field(name="$stream", value="Change what the bot is streaming", inline=False)
                    embed.add_field(name="$listen", value="Change what the bot is listening", inline=False)
                    embed.add_field(name="$watch", value="Change what the bot is watching", inline=False)
                    embed.set_footer(text="Made with ❤ by arki#8251")
                    await client.send_message(message.channel, embed=embed)
                    await client.add_reaction(message, emoji="✅")
                else:
                    await client.add_reaction(message, emoji="❎")



            if  message.content.lower().startswith('$say'):
                if message.author.id == "420777499627094036":
                    args = message.content.split(" ")
                    await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                    await client.delete_message(message)
                else:
                    await client.add_reaction(message, emoji="❎")



            if  message.content.lower().startswith('$play'):
                if message.author.id == "420777499627094036":
                    args = message.content.split(" ")
                    await client.change_presence(game=discord.Game(name= "%s" % (" ".join(args[1:])), type=0))
                    await client.add_reaction(message, emoji="✅")
                else:
                    await client.add_reaction(message, emoji="❎")



            if  message.content.lower().startswith('$stream'):
                if message.author.id == "420777499627094036":
                    args = message.content.split(" ")
                    await client.change_presence(game=discord.Game(name= "%s" % (" ".join(args[1:])), type=1))
                    await client.add_reaction(message, emoji="✅")
                else:
                    await client.add_reaction(message, emoji="❎")



            if  message.content.lower().startswith('$listen'):
                if message.author.id == "420777499627094036":
                    args = message.content.split(" ")
                    await client.change_presence(game=discord.Game(name= "%s" % (" ".join(args[1:])), type=2))
                    await client.add_reaction(message, emoji="✅")
                else:
                    await client.add_reaction(message, emoji="❎")



            if  message.content.lower().startswith('$watch'):
                if message.author.id == "420777499627094036":
                    args = message.content.split(" ")
                    await client.change_presence(game=discord.Game(name= "%s" % (" ".join(args[1:])), type=3))
                    await client.add_reaction(message, emoji="✅")
                else:
                    await client.add_reaction(message, emoji="❎")








client = MyClient()

client.run('key?')
