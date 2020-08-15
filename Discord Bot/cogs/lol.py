import discord
from discord.ext import commands
from riotwatcher import LolWatcher, ApiError

api_key = 'key'

class League(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def find(self, ctx, arg):
        watcher = LolWatcher(api_key)
        my_region = 'na1'

        me = watcher.summoner.by_name(my_region, arg)
        latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
        static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
        static_item_list = watcher.data_dragon.items(latest, 'en_US')
        my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
        last_match = my_matches['matches'][0] #specify the match #, change later for arg
        match_detail = watcher.match.by_id(my_region, last_match['gameId'])
        participants, temp = [], []

        i = 0
        for name in match_detail['participantIdentities']:
            temp.append(name['player']['summonerName'])

        for row in match_detail['participants']:
            participants_row = {}

            i0 = row['stats']['item0']
            i1 = row['stats']['item1']
            i2 = row['stats']['item2']
            i3 = row['stats']['item3']
            i4 = row['stats']['item4']
            i5 = row['stats']['item5']

            try:
                participants_row['item0'] = static_item_list['data'][str(i0)]['name']
            except:
                participants_row['item0'] = None
            try:
                participants_row['item1'] = static_item_list['data'][str(i1)]['name']
            except:
                participants_row['item1'] = None
            try:
                participants_row['item2'] = static_item_list['data'][str(i2)]['name']
            except:
                participants_row['item2'] = None
            try:
                participants_row['item3'] = static_item_list['data'][str(i3)]['name']
            except:
                participants_row['item3'] = None
            try:
                participants_row['item4'] = static_item_list['data'][str(i4)]['name']
            except:
                participants_row['item4'] = None
            try:
                participants_row['item5'] = static_item_list['data'][str(i5)]['name']
            except:
                participants_row['item5'] = None

            g = match_detail['gameDuration']
            g = (g//60) + ((g % 60)/100)
            participants_row['game duration'] = "{:.2f}".format(g)
            #participants_row['total Minions Killed'] = row['stats']['totalMinionsKilled']
            participants_row['Summoner Name'] = temp[i]
            participants.append(participants_row)

            i += 1

        arr = {}

        embed = discord.Embed(colour = discord.Color.blue())

        for i in participants:
            arr[str(i['Summoner Name'])] = i 

        for i in temp:
            embed.add_field(name=i, value = str(arr[str(i)]['item0']) + "\n" + str(arr[str(i)]['item1']) + "\n" + str(arr[str(i)]['item2'])  + "\n" + str(arr[str(i)]['item3'])  + "\n" + str(arr[str(i)]['item4'])  + "\n" + str(arr[str(i)]['item5']), inline=False)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            embed.set_footer(text = ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(League(client))