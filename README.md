## vprwbot
### ａｄｄ　ａ　ｔｏｕｃｈ　ｏｆ　ａｅｓｔｈｅｔｉｃ　ｔｏ　ｙｏｕｒ　ｔｅｌｅｇｒａｍ　ｅｘｐｅｒｉｅｎｃｅ　だ彙っ援中ょ暗ボ威
This is a simple inline bot to make aesthetic messages

### Requirements
- Python 3.6 (it _should_ work with every other 3.x as well)  
- pip  
- virtualenv (`pip install virtualenv`)  

### Installation
[Ｔｈｅｒｅ＇ｓ　ａｎ　ａｅｓｔｈｅｔｉｃ　ｉｎｓｔａｌｌａｔｉｏｎ　ｇｕｉｄｅ　ｉｎ　ａ　ＶＨＳ　ｆａｓｈｉｏｎ　ｓｔｒａｉｇｈｔ　ｆｒｏｍ　ｔｈｅ　８０ｓ　ａｖａｉｌａｂｌｅ　ｈｅｒｅ．　煙鬱延ー　印凹仮　イ　援さ位横ー真ヵ](https://youtu.be/t2x91807C4A)  


### If you prefer a boring text version, here you go:
1. Create a telegram bot with @BotFather and copy the API token  
2. Run these commands (assuming you're using a linux server)  
```bash
$ git clone ...
$ cd vprwbot
$ virtualenv -p $(which python3.6) .pyenv
$ source .pyenv/bin/activate
(.pyenv)$ pip install -r requirements.txt
(.pyenv)$ cp settings.sample.ini settings.ini
(.pyenv)$ nano settings.ini
[paste your telegram bot token, save and exit]
(.pyenv)$ python vprw.py
ｖｐｒｗ　＠　１．０．０
ｍａｄｅ　ｂｙ　ｎｙｏ

INFO:vprw:Ｂｏｔ　ｓｔａｒｔｅｄ！  つャャ
```
3. Run `/setinline` on @BotFather, select your bot and type whatever you want as inline query placeholder
**NOTE: You should use tmux, screen, nohup, a service or whatever you want to run your bot or it'll stop working
when you close your ssh terminal window!**

### Usage
This bot has only a `/start` command with general information.  
To make your messages ａｅｓｔｈｅｔｉｃ　タくラ, use it as an inline bot.  
A live example of this bot is available at @vprwbot.  
Type this in any chat:  
```
@vprwbot lorem ipsum
```
And you'll receive different ａｅｓｔｈｅｔｉｃ　王維穏 variants of your messages.  
Click the one you like and ｆｅｅｌ　ｔｈｅ　ａｅｓｔｈｅｔｉｃ　ｉｎ　ｙｏｕｒ　ｃｈａｔ　タ無コィヤゼ.  
ｓｉｍｐｌｅ　ａｓ　ｔｈａｔ　唄佳ア (:new_moon_with_face:)  

### License
MIT. Check the `LICENSE` file for more information.