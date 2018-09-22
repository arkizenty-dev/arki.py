# imports modules used

import discord
import platform
import time
import random



python_version=platform.python_version()
start_time=time.asctime()


# a~arki quotes

quotes = ['For some reason, people started calling me a "markov-bot clone"',
          'I have started running on a raspberry pi now, but I feel a lot slower now',
          'Someday I will say something useful things, but for now I can not think of any',
          'I wonder when arkizenty is going to add anything useful...',
          'Heh, I can run 24/7 now',
          'I wonder how arkizenty is doing...',
          '~time',
          'Showouts to simple flips!',
          'This is boring...',
          f'How are you doing?',
          f'~arki.py Lemme check the Python version...']
random.shuffle(quotes)



# ~jokes quotes

jokes = ['I told my wife she was drawing her eyebrows too high. She looked surprised. ```Joke created by Scrappy_Larue https://www.reddit.com/r/AskReddit/comments/2f17dv/whats_your_best_two_line_joke/ck538op```',
         'My grandpas last words before kicking the bucket.  Grandpa: I wonder how far I can kick this bucket ```Joke created by ??? https://www.reddit.com/r/AskReddit/comments/3d08ds/whats_your_favourite_one_or_twoline_joke/ct0oexz```']
random.shuffle(jokes)




class MyClient(discord.Client):
    async def on_ready(self):
        print (f'Currently running on Python Version {python_version}')
        print(f'Now running arki.py since {start_time}!'.format(self.user))

        @client.event
        async def on_message(message):

            # Response's towards users

            if message.content.lower() == "hi":
                await  client.send_message(message.channel, f'Hello there {message.author.mention}! :D')
                print(f'{message.author} said hi on {start_time}')

            if message.content.lower() == "hola":
                await client.send_message(message.channel, f'Hello there {message.author.mention}! :D')
                print(f'{message.author} said hola on {start_time}')

            if message.content.lower() == "hello":
                await client.send_message(message.channel, f'Hello there {message.author.mention}! :D')
                print(f'{message.author} said hello on {start_time}')

            if message.content.lower() == "hello!":
                await client.send_message(message.channel, f'Hello there {message.author.mention}! :D')
                print(f'{message.author} said hello! on {start_time}')

            if message.content.lower() == "gay":
                await client.send_message(message.channel, 'no u')
                print(f'{message.author} said gay on {start_time}')

            if message.content.lower() == "gae":
                await client.send_message(message.channel, 'no u')
                print(f'{message.author} said gae on {start_time}')



            # Regular Commands

            if message.content.lower() == "~ping":
                await client.send_message(message.channel, ':ping_pong: Pong! :ping_pong:')
                print(f'{message.author} used ~ping on {start_time}')

            if message.content.startswith('~help'):
                await client.send_message(message.channel, '```~ping - Pong!```'
                                                           '```~help - Shows a list of commands```'
                                                           '```~about - Shows info about arki.py + github page```'
                                                           '```~arki.py - Shows info on what version of Python is running and what version arki.py is currently on```'
                                                           '```~time - Shows the date and time```'
                                                           '```~secrets - Shows the secret commands (Via Direct Messages)```')
                print(f'{message.author} used ~help on {start_time}')

            if message.content.startswith('~secrets'):
                await client.send_message(message.author, '```~relax - ???```'
                                                           '```~pour - ???```'
                                                           '```@someone - ???```'
                                                          '```a~arki - Makes the bot say *useful* things```'
                                                          '```~joke - Tells a joke to the user```')
                print(f'{message.author} used ~secrets on {start_time}')

            if message.content.startswith('~about'):
                await client.send_message(message.channel, 'arki.py is a bot created by arkizenty#7140 created to interact with users. Github: https://github.com/arkizenty/arki.py')
                print(f'{message.author} used ~about on {start_time}')

            if message.content.startswith('~arki.py'):
                await client.send_message(message.channel, f'```Currently v1.0 running Python Version {python_version}```')
                print(f'{message.author} used ~arki.py on {start_time}')

            if message.content.startswith('~time'):
                await client.send_message(message.channel,
                                          f'```Currently {start_time}```')
                print(f'{message.author} used ~time on {start_time}')



            # Secret Commands

            if message.content.startswith('~relax'):
                await client.send_message(message.channel, f'Ｒ　ｅ　Ｌ　ａ　ｘ　 {message.author.mention} https://youtu.be/WYUOKnZkgko')
                print(f'{message.author} used ~relax on {start_time}')

            if message.content.startswith('~pour'):
                await client.send_message(message.channel, 'https://youtu.be/IJ-PVdapaDU')
                print(f'{message.author} used ~pour on {start_time}')

            if message.content.startswith('@someone'):
                await client.send_message(message.channel, 'https://youtu.be/BeG5FqTpl9U')
                print(f'{message.author} used @someone on {start_time}')

            if message.content.startswith('a~arki'):
                await client.send_message(message.channel, random.choice(quotes))
                print(f'{message.author} used a~arki on {start_time}')

            if message.content.startswith('~joke'):
                await client.send_message(message.channel, random.choice(jokes))
                print(f'{message.author} used ~joke on {start_time}')




client = MyClient()

client.run('Put a token here arki')
