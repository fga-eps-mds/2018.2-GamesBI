from CrossData.API.models import *

steam_attrs = list(vars(InfoSteam()).keys())
youtube_attrs = list(vars(InfoYoutube()).keys())
twitch_attrs = list(vars(InfoTwitch()).keys())
streams_attrs = list(vars(TwitchStream()).keys())
