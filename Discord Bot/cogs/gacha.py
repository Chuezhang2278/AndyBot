import discord
import json
from discord.ext import commands
from ArkUnits import *


class Gacha(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rates(self,ctx):
        await ctx.send('3★ = 40%, 4★ = 50%, 5★ = 8%, 6★ = 2%')

    @commands.command()
    async def roll(self, ctx):

        f = open('data.json',)
        data = json.load(f)
        Arknights_Pool = Pool()
        
        for i in data['Units']:
            Arknights_Pool.addPool(i)
        
        res = Arknights_Pool.roll()
        await ctx.send(f'```\n\tResults\n================\n{res}```')

def setup(client):
    client.add_cog(Gacha(client))