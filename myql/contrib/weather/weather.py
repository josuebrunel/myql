from __future__ import absolute_import

from myql.myql import YQL


class Weather(YQL):
    """Weather Class
    """

    def __init__(self, unit=None, **kwargs):
        """Initialize a weather object
        """
        kwargs.update({'community': False})

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
        response = self.get_weather_in(place, items=['item.forecast'], unit=unit)
        return response        

    def get_weather_description(self, place):
        """Return weather description 
        """
        response = self.get_weather_in(place, items=['item.condition.text'])
        return response

    def get_current_condition(self, place):
        """Return weather condition
        """
        response = self.get_weather_in(place, items=['item.condition'])
        return response

    def get_current_atmosphere(self, place):
        """Return weather atmosphere
        """
        response = self.get_weather_in(place, items=['atmosphere'])
        return response

    def get_current_wind(self, place):
        """Return weather wind  
        """
        response = self.get_weather_in(place, items=['wind'])
        return response

    def get_astronomy(self, place):
        """Return sunrise and sunset time
        """
        response = self.get_weather_in(place, items=['astronomy'])
        return response
