from __future__ import absolute_import

from myql.myql import YQL


class Weather(YQL):
    """Weather Class
    """

    def __init__(self, *args, **kwargs):

        super(Weather, self).__init__(**kwargs)


    def get_weather_in(self, place):
        """Return weather info according to place
        """
        response = self.select('weather.forecast').where(['woeid','IN',('SELECT woeid FROM geo.places WHERE text="{0}"'.format(place),)])
        return response
