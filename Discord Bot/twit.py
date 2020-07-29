# used to test twitter API stuff

import tweepy
import os

consumer_key = 'key'
consumer_secret = 'key'

access_token = 'token'
access_token_secret = 'token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#print(dir(api))

user = api.get_user("asdashuda")
#print(dir(user))
#print(user.id)
user_timeline = user.timeline()
user_timeline_status_obj = user_timeline[0] #First tweet on their timeline
status_obj_id = user_timeline_status_obj.id #tweet ID

status_obj = api.get_status(status_obj_id) #Status of ID
#print(status_obj.text) #Printing out ID

#api.create_friendship(user.screen_name) #following people
#print(user.screen_name)
#api.destroy_friendship('PCGamesN') #How to remove

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        file = open("tweet.txt", "w")
        with open("tweet.txt","a") as f:
            f.write(status.text)
        f.close()
        print(status.text)

    def process_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

class CreateStream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth = auth, listener = listener)
    
    def start(self, keyworld_list):
        self.stream.filter(follow=keyworld_list)

listener = MyStreamListener()
stream = CreateStream(auth,listener)
stream.start(['3050330837'])

'''
query_username = "nekomataokayu"

def process_page(page_results):
    for i, test in enumerate(page_results):
        print(i, test.screen_name)
    
query_username = "nekomata"
search_results = set()
for user in (tweepy.Cursor(api.search_users, q=query_username).items(50)):
    search_results.add(user.screen_name)

for i, item in enumerate(search_results):
    print(i, item)

query_username = 'nekomataokayu'
search_results = set()
for user in (tweepy.Cursor(api.search_users, q=query_username).items(10)):
    search_results.add(user.screen_name)

temp = '\n'.join(list(search_results))

print(f"```{temp}```")

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

img_obj = api.media_upload("pprCvO3.png")
new_status = api.update_status("test img", media_ids=[img_obj.media_id_string])
'''