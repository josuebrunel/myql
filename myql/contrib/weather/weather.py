from __future__ import absolute_import

from myql.myql import YQL


class Weather(YQL):
    """Weather Class
    """

    def __init__(self, unit=None, **kwargs):
        """Initialize a weather object
        """
        kwargs.update({'community':False})

        super(Weather, self).__init__(**kwargs)

        self.unit = unit 


    def get_weather_in(self, place, unit=None, items=None):
        """Return weather info according to place
        """
        unit = unit if unit else self.unit
        response = self.select('weather.forecast', items=items).where(['woeid','IN',('SELECT woeid FROM geo.places WHERE text="{0}"'.format(place),)], ['u','=',unit] if unit else [])
        return response

    def get_weather_forecast(self, place, unit=None):
        """Return weather forecast accoriding to place
        """
        unit = unit if unit else self.unit
        response = self.select('weather.forecast', items=['item.forecast']).where(['woeid','IN',('SELECT woeid FROM geo.places WHERE text="{0}"'.format(place),)], ['u','=',unit] if unit else [])
        return response        
