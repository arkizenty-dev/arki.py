import discord
import platform
python_version=platform.python_version()



class MyClient(discord.Client):
    async def on_ready(self):
        print (f'Currently running on Python Version {python_version}')
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        @client.event
        async def on_message(message):
            if message.content.lower() == "hi":
                await  client.send_message(message.channel, f'Hello there {message.author}! :D')
                print(f'{message.author} said hi')

            if message.content.lower() == "hola":
                await client.send_message(message.channel, f'Hello there {message.author}! :D')
                print(f'{message.author} said hola')

            if message.content.lower() == "hello":
                await client.send_message(message.channel, f'Hello there {message.author}! :D')
                print(f'{message.author} said hello')

            if message.content.lower() == "gay":
                await client.send_message(message.channel, 'no u')
                print(f'{message.author} said gay')

            if message.content.lower() == "~ping":
                await client.send_message(message.channel, ':ping_pong: Pong! :ping_pong:')
                print(f'{message.author} used ~ping')

            if message.content.startswith('~help'):
                await client.send_message(message.channel, '```~help - Shows a list of commands```'
                                                           '```~test - Shows an invite link to the bot testing ground```'
                                                           '```~invite - Shows a link to invite arki.py```'
                                                           '```~about - Shows info about arki.py```'
                                                           '```~arki.py - Shows info on what version of Python is running and what version arki.py is currently on```')
                print(f'{message.author} used ~help')

            if message.content.startswith('~test'):
                await client.send_message(message.channel, 'Here is the test server link https://discord.gg/pkr4p2z')
                print(f'{message.author} used ~test')

            if message.content.startswith('~invite'):
                await client.send_message(message.channel, 'Here is the invite link! Thanks for asking for the invite! https://discordapp.com/oauth2/authorize?client_id=484539869922590721&permissions=116736&scope=bot')
                print(f'{message.author} used ~invite')

            if message.content.startswith('~about'):
                await client.send_message(message.channel, 'arki.py is a bot created by arkizenty#7140 created to interact with users.')
                print(f'{message.author} used ~about')

            if message.content.startswith('~arki.py'):
                await client.send_message(message.channel, f'```Currently v0.9 Beta running Python Version {python_version}```')
                print(f'{message.author} used ~arki.py')

            if message.content.startswith('~relax'):
                await client.send_message(message.channel, f'Ｒ　ｅ　Ｌ　ａ　ｘ　 {message.author} https://youtu.be/WYUOKnZkgko')
                print(f'{message.author} used ~relax')

            if message.content.startswith('~pour'):
                await client.send_message(message.channel, 'https://youtu.be/IJ-PVdapaDU')
                print(f'{message.author} used ~pour')

            if message.content.startswith('@someone'):
                await client.send_message(message.channel, 'https://youtu.be/BeG5FqTpl9U')
                print(f'{message.author} used @someone')





client = MyClient()

client.run('Put a token here arki')
