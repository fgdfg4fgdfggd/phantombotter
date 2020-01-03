from plugin import Plugin
import random

class Git(Plugin):

    fancy_name='Site'

    async def get_commands(self, server):
        commands = [
            {
                'name': '!site',
                'description': 'Links to RCDForunm page.'
            },
        ]
        return commands

    async def on_message(self, message):

        flavortext = [
            "Glad you asked!",
            "Hey kid, wanna see our site?",
            "Thanks for stopping by!",
            "Here's where the RCD Magic happens."
            ]

        if message.content == '!site':
            await self.mee6.send_message(
                message.channel,
                '{}\nhttps://rcdforum.com/'.format(
                random.choice(flavortext)
                )
             )
