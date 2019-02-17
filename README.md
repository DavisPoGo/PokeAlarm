![PokeAlarm](https://raw.githubusercontent.com/wiki/PokeAlarm/PokeAlarm/images/logo.png)
[![Discord](https://discordapp.com/api/guilds/215181169761714177/widget.png?style=shield)](https://discord.gg/S2BKC7p)
[![Donate](https://img.shields.io/badge/Donate-Patron-orange.svg)](https://www.patreon.com/bePatron?u=5193416)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![license](https://img.shields.io/github/license/PokeAlarm/PokeAlarm.svg)

### How to use the OneManager branch

####Overview:
This PA modification allows you to run all your alerts with 1 manager. It accomplishes this by three main additions
1) All the filters get checked. For each filter that is matched, an alarm is triggered
2) All matching geofence(s) for each event can trigger an alarm. (you do not need a duplicated filter set for each geofence)
3) A new file, channel_id.json, is required. This file translates your geofence+filter combination into the channel/webhook portion of the discord webhook url


channel_id.json, filters.json, and geofence.txt are all required and must all be formatted appropriately to make alerts work. 

See examples files to see an example set up similar to the one I use.

####geofence.txt

1) Formatted exactly the same as always.
2) The area names (ie [Area1]) must match the Area names used in channel_id.json
3) Do not set a geofence for "All". If an event matches any geofence, an alarm is also created for the corresponding Filter/Discord webhook url pair in the "All" key of channel_id.json.
4) Use SubAreas if you have multiple smaller areas within a larger area. For example, you have a discord channel for all ultra rare spawns within a city and you also have multiple channels for rare spawns occuring in each of many different neighborhoods within that city. In your geofence file, do not specify a geofence for [Area2], instead only specify geofences for each SubArea in the format [Area2-SubArea1]


####channel_id.json

- This file should look a lot like the organization of your discord server. See the example file for format. Some important points: 
1) You can include an "All" key, if an event occurs within any geofence, it can trigger an alarm using the "All" set of Filter names
2) The first dictionary level are Area/Filter pairs. The Area name in this file must must match the Area names used in geofence.txt
3) The second dictionary level are Filter/Discord Webhook Url pairs. The Filter name must match the Filter names in filters.json. The Discord Webhook Url is the last portion of the webhook url (ie everything after "discordapp.com/api/webhooks/" ) for the channel you want to send the alarm to.


####filters.json

1) No format changes from standard PA
2) Do not use '"geofences": [ "Area" ]'. All geofences supplied in geofences.txt will be checked for every event
3) The Filter name must match the Filter name specified in channel_id.json. (Except as described below)
4) In setting the Filter name the hyphen character (ie "-"), has a special use. If you have multiple filters you want to send to one discord channel you can use the hyphen to have different Filter names in filters.json that will match the same Filter name in channel_id.json. For example, in filters.json the Filter name "UltraRare-1" and "UltraRare-2" will both match the "UltraRare" key in channel_id.json. Thus, an event matching the conditions for either filter "UltraRare-1" or "UltraRare-2" will use the same Discord Webhook url.

####alarms.json

1) Do not include '"webhook_url":"YOUR_WEBHOOK_URL"' in alarms.json
2) Make sure your alarm format is robust enough to accomidate all filters. Only 1 alarm file is used




PokeAlarm is a highly configurable application that filters and relays alerts about PokemonGo to your favorite online service, allowing you to be first to know of any rare spawns or raids.

### Patch Notes
Recently updated? Make sure to check out the [Patch Notes](https://github.com/PokeAlarm/PokeAlarm/wiki/patch-notes) to help you get caught up on what has changed between versions.

## What exactly is PokeAlarm?
PokeAlarm is an easy to use yet highly configurable webserver designed to receive webhook data (via POST requests) from a scanner. PokeAlarm then filters data, and relays it into one of your favorite online services such as Discord, Twitter, and more. With PokeAlarm, you'll instantly know about every rare spawn or legendary raid that spawns on your scanners. It's highly configurable, allowing the user to define custom messages and filter alerts based on numerous criteria.

## Looking for Help?

#### Wiki
Head on over to the [**PokeAlarm Wiki**](http://pa.readthedocs.io/en/master/) to find detailed instructions on setting up and configuring PokeAlarm. You can find the table of contents on the right!

#### Discord
Before visiting your discord channel, check both the [Wiki](http://pa.readthedocs.io/en/master/) and the [FAQ](https://github.com/PokeAlarm/PokeAlarm/wiki/faq). If you still can't find what you are looking for, try our [**Discord channel**](https://discord.gg/S2BKC7p) - but make sure you read the **#rules** channel or risk getting banned!

#### Github
Have an idea for a new feature? Think you found a bug? Head over to our [Github](https://github.com/PokeAlarm/PokeAlarm/issues/new) and open an 'Issue' ticket. Make sure to follow the template completly, or else your issue will be closed without comment.

## Want to contribute?
Besides financial support, you can also do your part to help PA grow. Feel free to submit PR's to our [Github](https://github.com/PokeAlarm/PokeAlarm/issues/new). You can also suggest changes to the Wiki on our [Wiki Github](https://github.com/PokeAlarm/PokeAlarmWiki). If you find a mistake but don't have the skill to fix it, feel free to open an 'Issue' on the appropriate Github page.
