# Standard Library Imports
from datetime import datetime
# 3rd Party Imports
# Local Imports
from PokeAlarm import Unknown
from . import BaseEvent
from PokeAlarm.Utils import get_gmaps_link, get_applemaps_link, \
    get_time_as_str, get_seconds_remaining, get_dist_as_str


class StopEvent(BaseEvent):
    """ Event representing the discovery of a PokeStop. """

    def __init__(self, data):
        """ Creates a new Stop Event based on the given dict. """
        super(StopEvent, self).__init__('stop')
        check_for_none = BaseEvent.check_for_none

        # Identification
        self.stop_id = data['pokestop_id']
        self.stop_name = data['name']
        self.url = data['url']

        # Time left
        self.expiration = check_for_none(float, data.get('lure_expiration'), 0)
        self.time_left = None
        if self.expiration is not None:
            self.expiration = datetime.utcfromtimestamp(self.expiration)
            self.time_left = get_seconds_remaining(self.expiration)

        # Location
        self.lat = float(data['latitude'])
        self.lng = float(data['longitude'])

        # Completed by Manager
        self.distance = Unknown.SMALL
        self.direction = Unknown.TINY

        # Used to reject
        self.name = self.stop_id
        self.geofence = Unknown.REGULAR
        self.geofence_list = []
        self.custom_dts = {}
        self.channel_id = Unknown.REGULAR
        self.quest = data['quest']
        self.reward = data['reward']

        self.discord_user_id = check_for_none(int, data.get('discord_user_id'), 0)

    def generate_dts(self, locale, timezone, units):
        """ Return a dict with all the DTS for this event. """
        time = get_time_as_str(self.expiration, timezone)
        dts = self.custom_dts.copy()
        dts.update({
            # Identification
            'stop_id': self.stop_id,
            'stop_name': self.stop_name,
            'stop_url': self.url,

            # Time left
            'time_left': time[0],
            '12h_time': time[1],
            '24h_time': time[2],

            # Location
            'lat': self.lat,
            'lng': self.lng,
            'lat_5': "{:.5f}".format(self.lat),
            'lng_5': "{:.5f}".format(self.lat),
            'distance': (
                get_dist_as_str(self.distance, units)
                if Unknown.is_not(self.distance) else Unknown.SMALL),
            'direction': self.direction,
            'gmaps': get_gmaps_link(self.lat, self.lng),
            'applemaps': get_applemaps_link(self.lat, self.lng),
            'geofence': self.geofence,
            'geofence_list': self.geofence_list,
            'channel_id': self.channel_id,
            'quest': self.quest,
            'reward': self.reward,
            'submission_phrase':  ("\n**Submitted by: <@&" + str(self.discord_user_id) + ">" if self.discord_user_id > 0 else "")
        })
        return dts
