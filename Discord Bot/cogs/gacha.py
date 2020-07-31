import discord
import random
import os
from discord.ext import commands

class Gacha(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self, ctx):

        numlist = []

        for x in range(4):
            file = os.path.join('Gacha', 'AK{}.txt'.format(x+1))
            with open(file, 'r',) as f:
                f_read = f.read().splitlines()
                numlist.append(f_read)
                for i in range(len(numlist[x])):
                    numlist[x][i] = numlist[x][i] + f' - {x+3} ★' #can definitely improve on this method but another time
        x = random.choices(numlist, weights=(40,50,8,2), k = 10)

        choices = []

        for i in range(len(x)):
            choices.append(random.choice(x[i])) 

        temp = '\n'.join(choices)
        await ctx.send(f'```\n\tResults\n================\n{temp}```')

def setup(client):
    client.add_cog(Gacha(client))