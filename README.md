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

## Some important stuff for development

- [Discord Developer Portal](https://discord.com/developers/applications) 
- [Twitter API](https://www.tweepy.org/) - Grab your auth keys for twitter [here](https://developer.twitter.com/en)
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
