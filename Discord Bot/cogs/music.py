import discord
import os
from discord.ext import commands
from discord.utils import get
import youtube_dl

# Will finish another time when i gain more experience working with discord bot

class MusicCog(commands.Cog):
    def __init__(self, music):
        self.music = music
    
    @commands.command(pass_context = True)
    async def join(self, ctx):
        connected = ctx.author.voice
        if connected:
            await connected.channel.connect()

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        connected = ctx.author.voice
        if connected is None:
            return "Not in any channels"
        await ctx.voice_client.disconnect()

def setup(music):
    music.add_cog(MusicCog(music))