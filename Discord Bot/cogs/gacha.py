import discord
import json
from discord.ext import commands
from ArkUnits import *


class Gacha(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rates(self,ctx):
        await ctx.send('```\n3★ = 40%, 4★ = 50%, 5★ = 8%, 6★ = 2%\n```')

    @commands.command()
    async def roll(self, ctx):

        f = open('data.json',)
        data = json.load(f)
        Arknights_Pool = Pool()
        
        for i in data['Units']:
            Arknights_Pool.addPool(i)
        
        res = Arknights_Pool.roll()
        embed = discord.Embed(colour = discord.Color.blue())
        embed.add_field(name='Your pulls', value = res, inline=False)
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        embed.set_footer(text = ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Gacha(client))