import discord
import tweepy
import os
from discord.ext import commands

consumer_key = 'insert key here'
consumer_secret = 'insert secret here'

access_token = 'insert token here'
access_token_secret = 'insert secret here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#===========================================================================#

class Tweeting(commands.Cog):
    def __init__(self, tweet):
        self.tweet = tweet

    @commands.command()
    async def tweet(self,ctx, *, args):
        new_status = api.update_status(args)
    
    @commands.command(aliases = ['status'])
    async def status_check(self,ctx):
        timeline = api.home_timeline()
        status_obj = timeline[0]
        status_obj_id = status_obj.id
        await ctx.send(api.get_status(status_obj_id).text)

    @commands.command()
    async def lookup(self,ctx,args):
        
        query_username = args
        search_results = set()
        for user in (tweepy.Cursor(api.search_users, q=query_username).items(10)):
            search_results.add(user.screen_name)

        temp = '\n'.join(list(search_results))

        await ctx.send(f'```\nQuery Similar Results\n ==========\n{temp}```')

    @commands.command(aliases = ['stream'])
    async def LiveFeed(self,ctx,arg):

        class MyStreamListener(tweepy.StreamListener):
            
            def on_status(self, status):
                print(status.text)

            def on_error(self, status_code):
                if status_code == 420:
                    #returning False in on_error disconnects the stream
                    return False
        try:
            user = api.get_user(arg)
            await ctx.send(f"Now streaming live feed of {user.screen_name}\n{user.profile_image_url} ")
            listener = MyStreamListener()
            stream = tweepy.Stream(auth = auth, listener = listener)
            stream.filter(follow = [str(user.id)], is_async=True)
        except:
            await ctx.send("Couldnt find user specified")

def setup(tweet):
    tweet.add_cog(Tweeting(tweet))