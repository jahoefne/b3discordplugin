## B3Discord Plugin
is a tiny [B3](http://forum.bigbrotherbot.net/) Plugin for broadcasting your online [Discord](https://discordapp.com/) users on your gamerserver.

B3 is a Python based Game Server Administration Software.
Discord is a novel Audio/Text chat system aiming to replace ts3 and skype for gaming clans.

### Installation
- copy `extplugins/b3discord.py` to your `b3/extplugins/` folder 
- copy `extplugins/conf/b3discord.xml` to your `b3/extplugins/conf` folder and change it to match your prefered settings.
- put the following line in the plugins section of your `b3.xml`:

  -  `<plugin name="b3discord" config="@b3/extplugins/conf/b3discord.xml"></plugin>`
 
 - restart b3