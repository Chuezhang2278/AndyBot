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
    async def sammy(self,ctx):
        responses = ['lmao tilted',
                    '0/3/0 10 minutes',
                    'WHAT ARE YOU SHOOTING AT? WHERE ARE YOU SHOOTING AT?',
                    'crouch walking',
                    'team killing']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command(aliases=['8ball','test'])
    async def ball(self, ctx, *, args):
        responses = ['Small PP energy',
                    'Big PP energy',
                    '5head',
                    '3head',
                    'nohead']
        await ctx.send(f'{random.choice(responses)}')
    
    @commands.command()
    async def toot(self,ctx):
        await ctx.send('https://cdn.betterttv.net/emote/5e6d656e8c0f5c3723a92908/3x')

    @commands.command()
    async def embedtemplate(self, ctx):
        embed = discord.Embed(
            title = 'Title',
            description = 'Description',
            colour = discord.Color.red(),
            url = "https://www.google.com"
        )
        embed.set_thumbnail(url='https://cdn.betterttv.net/emote/5e6d656e8c0f5c3723a92908/3x')
        embed.add_field(name='Text', value = 'Field Value', inline=True)
        embed.add_field(name='Text2', value = 'Field Value', inline=False)
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        embed.set_footer(text = ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Cogs(client))