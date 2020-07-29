import discord
import random
from discord.ext import commands

class Cogs(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status = discord.Status.idle, activity= discord.Game('Just chilling'))

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('Missing Arguments')
        if isinstance(error,commands.CommandNotFound):
            await ctx.send('Not a command')
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('pong')

    @commands.command()
    async def sammy(self,ctx):
        await ctx.send('lmao tilted')

    @commands.command(aliases=['8ball','test'])
    async def ball(self, ctx, *, args):
        responses = ['Small PP energy',
                    'Big PP energy',
                    '5head',
                    '3head',
                    'nohead']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def apos(self, ctx, args):
        await ctx.send(f'```\n{args}\n```')

def setup(client):
    client.add_cog(Cogs(client))