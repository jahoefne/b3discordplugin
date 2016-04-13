
__version__ = '0.0.1'
__author__ = 'jahoefen'

import threading
import time
import os
import b3
import b3.events
import b3.plugin
import json
import urllib2

class Vote:
    Vote = 0


# --------------------------------------------------------------------------------------------------
class B3DiscordPlugin(b3.plugin.Plugin):

    def onLoadConfig(self):
        try:
            self._discord_widget_url = self.config.getstring('settings', 'discord_widget_url')
        except:
            self._discord_widget_url = "127.0.0.1"
        try:
            self._repeat_interval = self.config.getint('settings', 'repeat_interval')
        except:
            self._repeat_seconds = 300
        self.CyclicListPlayers(self);

    def CyclicListPlayers(self):
        self._discord_widget_url = "https://discordapp.com/api/servers/162787891422953473/widget.json"
        # facking a user agent so discord gives us the json
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

        req = urllib2.Request(self._discord_widget_url, headers=hdr)

        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

        content = json.loads(str(page.read()))

        message = 'Right now online on our discord server: '
        for member in content['members']:
            message += member['username']
            message += ', '

        message = message[:-2]
        message += '. Come Join Us! :)'
        print(message)
        self.console.say( message)
        t = threading.Timer(self._repeat_interval, self.CyclicListPlayers)
        t.start()