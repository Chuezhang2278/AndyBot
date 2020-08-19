## What is this?

Looking to make a bot to harass and meme with my friends, still under heavy development. Bot is also up 24/7
> [Invite Link](https://discord.com/oauth2/authorize?client_id=734861397627764856&scope=bot)

## What it got?

- Seveal funky commands using apis listed
  - RiotAPI
  - Tweepy
  - YT_DL(nothing for this atm)
- Simple gacha system for the mobile phone game "Arknights"
- Basic discord manipulation commands

I am currently more invested in working with the RiotAPI at the moment because it is something i am a bit more familiar with and would like to learn more about since a lot of my friends play this game. Expect more from RiotAPI than the rest of the things listed

## Some important stuff for development

If you want to run my code, you have to get your own auth keys from the links listed below

- [Discord Developer Portal](https://discord.com/developers/applications) 
- [Twitter API](https://www.tweepy.org/) 
- [Rito Developer Portal](https://developer.riotgames.com/)

## Some requirements

template = pip install "blah"
- [riotwatcher](https://pypi.org/project/riotwatcher/1.3/)
- [youtube_dl](https://pypi.org/project/youtube_dl/)
- [tweepy](https://pypi.org/project/tweepy/)
- [discord.py](https://pypi.org/project/discord.py/)

Obviously you'll also need to download discord itself

- [discord](https://discord.com/)

## Log (as of 7/31)

### <ins>7/31</ins>

- Been playing [Arknights](https://www.arknights.global/) recently so i decided to make a bot for the **Gacha System**, all units not in the pool but it works well enough. 
  - **What is this Gacha System?** - Basically a lottery system in a game where there is a different set of items that you try to get using in game currency. Percentages are low and its quite easy to indulge yourself into these type of things if you are a gamer.
  
### <ins>8/02</ins>

Decided to learn a bit of json and things became a whole lot simpler and also familiarized myself more with python dicts. 

- Removed
  - Removed Gacha folder containing text files 
  - txt file read methods
  - Some test files
- Added
  - Json file uploaded and loading json file instead
  - Made a class file for organization purposes (ArkUnits.py)

### <ins>8/04</ins>

Discovered a thing

- WE GOT EMBEDDING NOW, much cleaner texts 

### <ins>8/05</ins>

Bot is now up 24/7, done free using [Heroku](https://www.youtube.com/watch?v=BPvg9bndP1U)

[Invite Link](https://discord.com/oauth2/authorize?client_id=734861397627764856&scope=bot)

### <ins>8/14</ins>

Decided to integrate Riot API with my discord bot. Many annoyances using this API because i suck at using it.

- Added
'$find (arg)' command that finds user specified and prints out information regarding latest match played
 
 ![Text](https://i.imgur.com/Pif5vVL.png)

### <ins>8/18</ins>
 
Working at 5 am is the best way to get things done. Big upgrade from item text to item icon which took an un-holy amount of time so if you want to(whoever is looking through this is interested in working with riotAPI), i highly recommend you just steal my itemlist.json file for icons. I think i died on the inside a little doing this but it was worth it.
 
![Text](https://i.imgur.com/uJtAWHX.png)

#### PART 2 OF 8/18

Further developed $find command to be more visually appealing but ran into an interesting issue that i currently have no knowledge on how to fix.

#### Bug
- Certain users won't have their information displayed, for example myself (ign = desuuuuuuuuuu) but others will. I have to test more to figure out whats the issue with this 

![Text](https://i.imgur.com/1dh8FMv.png)
