from plugin import Plugin
import discord
import os


class Mee6Game(Plugin):

    is_global = True
    game = os.getenv("RCDForum", 'rcdforum.com')

    async def on_ready(self):
        await self.mee6.change_presence(
            game=discord.Game(
                name=self.game
            )
        )
