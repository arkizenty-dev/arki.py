import discord
from googletrans import Translator
import platform
python_version=platform.python_version()


class Translate:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        try:
                if message.author.id == self.bot.user.id:
                    return
                detect = Translator().detect(message.content)
                # make it ignore english
                if detect.lang == 'en':
                    return
                # any other language, detected automatically
                elif detect.lang != 'sv':
                    async with message.channel.typing():
                        rewrite = Translator().translate(message.content)
                        final = Translator().detect(rewrite.text)

                    if final.lang == 'en':
                        await message.channel.send(rewrite.text)
                    else:
                        return

        except AttributeError:
            # Stop translations from working in PM

            detect = Translator().detect(message.content)
            if detect.lang:
                return


class MyClient(discord.Client):
    async def on_ready(self):
        print(python_version)
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        @client.event
        async def on_message(message):
            if message.content.lower() == "ping":
                await client.send_message(message.channel, 'pong')

            if message.content.lower() == "hi":
                await client.send_message(message.channel, 'Oh hey there user!')

            if message.content.lower() == "hola":
                await client.send_message(message.channel, 'Oh hey there user!')

            if message.content.lower() == "hello":
                await client.send_message(message.channel, 'Oh hey there user!')

            if message.content.lower() == "gay":
                await client.send_message(message.channel, 'no u')

            if message.content.startswith('!help'):
                await client.send_message(message.channel, 'oof, no code due to bugs. Will get patched in the future')

            if message.content.startswith('!test'):
                await client.send_message(message.channel, 'Here is the test server link https://discord.gg/pkr4p2z')

            if message.content.startswith('!invite'):
                await client.send_message(message.channel, 'Here is the invite link! Thanks for asking for the invite! https://discordapp.com/oauth2/authorize?client_id=484539869922590721&permissions=116736&scope=bot')

            if message.content.startswith('!about'):
                await client.send_message(message.channel, 'arki is a bot created by arkizenty#7140 for use for servers.')

            if message.content.startswith('!roast'):
                await client.send_message(message.channel, 'lmao, that was a great time! https://cdn.discordapp.com/attachments/422293824770146306/484896273258905612/Screenshot_from_2018-08-30_18-16-03.png')

            if message.content.startswith('!arki.py'):
                await client.send_message(message.channel, 'Currently v0.1 Beta')

            if message.content.startswith('!deki'):
                await client.send_message(message.channel, python_version)


client = MyClient()

client.run('TOKEN')