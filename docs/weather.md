Weater
=======

### **Definition**

####*Weather(unit=None, **kwargs**)*

* ***unit*** : alternative to default is **c**
* ***kwargs*** : Any possible argument of **YQL**

```python
from myql.contrib.weather import Weather
weather = Weather(unit='c', format='json')
```


### **Methods**

#### *Weather.get_weather_in(place, unit=None, items=None)*
>Return weather information according to the place passed in

```python
data = weather.get_weather_in('choisy-le-roi', 'c',['location', 'units', 'item.condition'])
```

```json
{
    "query": {
        "count": 1, 
        "created": "2015-07-08T08:34:05Z", 
        "lang": "en-US", 
        "results": {
            "channel": {
                "astronomy": {
                    "sunrise": "5:55 am", 
                    "sunset": "9:53 pm"
                }, 
                "atmosphere": {
                    "humidity": "59", 
                    "pressure": "1015.92", 
                    "rising": "0", 
                    "visibility": "9.99"
                }, 
                "description": "Yahoo! Weather for Choisy-le-Roi, FR", 
                "image": {
                    "height": "18", 
                    "link": "http://weather.yahoo.com", 
                    "title": "Yahoo! Weather", 
                    "url": "http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif", 
                    "width": "142"
                }, 
                "item": {
                    "condition": {
                        "code": "30", 
                        "date": "Wed, 08 Jul 2015 10:00 am CEST", 
                        "temp": "18", 
                        "text": "Partly Cloudy"
                    }, 
                    "description": "\n<img src=\"http://l.yimg.com/a/i/us/we/52/30.gif\"/><br />\n<b>Current Conditions:</b><br />\nPartly Cloudy, 18 C<BR />\n<BR /><b>Forecast:</b><BR />\nWed - Cloudy. High: 22 Low: 13<br />\nThu - Partly Cloudy. High: 25 Low: 11<br />\nFri - Sunny. High: 28 Low: 13<br />\nSat - Mostly Sunny. High: 31 Low: 13<br />\nSun - Partly Cloudy. High: 25 Low: 15<br />\n<br />\n<a href=\"http://us.rd.yahoo.com/dailynews/rss/weather/Choisy-le-Roi__FR/*http://weather.yahoo.com/forecast/FRXX3747_c.html\">Full Forecast at Yahoo! Weather</a><BR/><BR/>\n(provided by <a href=\"http://www.weather.com\" >The Weather Channel</a>)<br/>\n", 
                    "forecast": [
                        {
                            "code": "26", 
                            "date": "8 Jul 2015", 
                            "day": "Wed", 
                            "high": "22", 
                            "low": "13", 
                            "text": "Cloudy"
                        }, 
                        {
                            "code": "30", 
                            "date": "9 Jul 2015", 
                            "day": "Thu", 
                            "high": "25", 
                            "low": "11", 
                            "text": "Partly Cloudy"
                        }, 
                        {
                            "code": "32", 
                            "date": "10 Jul 2015", 
                            "day": "Fri", 
                            "high": "28", 
                            "low": "13", 
                            "text": "Sunny"
                        }, 
                        {
                            "code": "34", 
                            "date": "11 Jul 2015", 
                            "day": "Sat", 
                            "high": "31", 
                            "low": "13", 
                            "text": "Mostly Sunny"
                        }, 
                        {
                            "code": "30", 
                            "date": "12 Jul 2015", 
                            "day": "Sun", 
                            "high": "25", 
                            "low": "15", 
                            "text": "Partly Cloudy"
                        }
                    ], 
                    "guid": {
                        "content": "FRXX3747_2015_07_12_7_00_CEST", 
                        "isPermaLink": "false"
                    }, 
                    "lat": "48.76", 
                    "link": "http://us.rd.yahoo.com/dailynews/rss/weather/Choisy-le-Roi__FR/*http://weather.yahoo.com/forecast/FRXX3747_c.html", 
                    "long": "2.42", 
                    "pubDate": "Wed, 08 Jul 2015 10:00 am CEST", 
                    "title": "Conditions for Choisy-le-Roi, FR at 10:00 am CEST"
                }, 
                "language": "en-us", 
                "lastBuildDate": "Wed, 08 Jul 2015 10:00 am CEST", 
                "link": "http://us.rd.yahoo.com/dailynews/rss/weather/Choisy-le-Roi__FR/*http://weather.yahoo.com/forecast/FRXX3747_c.html", 
                "location": {
                    "city": "Choisy-le-Roi", 
                    "country": "France", 
                    "region": ""
                }, 
                "title": "Yahoo! Weather - Choisy-le-Roi, FR", 
                "ttl": "60", 
                "units": {
                    "distance": "km", 
                    "pressure": "mb", 
                    "speed": "km/h", 
                    "temperature": "C"
                }, 
                "wind": {
                    "chill": "18", 
                    "direction": "270", 
                    "speed": "25.75"
                }
            }
        }
    }
}

```

#### *Weather.get_weather_forecast(place, unit=None)*
>Return weather forecast

```python
data = weather.get_weather_description('dolisie')
```

```json
{
    "query": {
        "count": 1, 
        "created": "2015-07-08T08:35:27Z", 
        "lang": "en-US", 
        "results": {
            "channel": {
                "item": {
                    "condition": {
                        "text": "Cloudy"
                    }
                }
            }
        }
    }
}

```

#### *Weather.get_current_atmosphere(place)*
>Return weather atmosphere

```python
data = weather.get_current_condition('Nantes')
```

```json
{
        "count": 4, 
        "created": "2015-07-08T08:38:17Z", 
        "lang": "en-US", 
        "results": {
            "channel": [
                {
                    "item": {
                        "condition": {
                            "code": "28", 
                            "date": "Wed, 08 Jul 2015 10:00 am CEST", 
                            "temp": "18", 
                            "text": "Mostly Cloudy"
                        }
                    }
                }, 
                {
                    "item": {
                        "condition": {
                            "code": "3200", 
                            "date": "Wed, 08 Jul 2015 4:00 am EDT", 
                            "temp": "19", 
                            "text": "Unknown"
                        }
                    }
                }, 
                {
                    "item": {
                        "condition": {
                            "code": "27", 
                            "date": "Wed, 08 Jul 2015 5:01 am BRT", 
                            "temp": "16", 
                            "text": "Mostly Cloudy"
                        }
                    }
                }, 
                {
                    "item": {
                        "condition": {
                            "code": "28", 
                            "date": "Wed, 08 Jul 2015 7:58 am WEST", 
                            "temp": "18", 
                            "text": "Mostly Cloudy"
                        }
                    }
                }
            ]
        }
    }
}

```

#### *Weather.get_current_atmosphere(place)*
>Return sunrise and sunset time

```python
data = weather.get_current_atmosphere('Scotland')
```

```json
{
    "query": {
        "count": 10, 
        "created": "2015-07-08T08:43:26Z", 
        "lang": "en-US", 
        "results": {
            "channel": [
                {
                    "atmosphere": {
                        "humidity": "95", 
                        "pressure": "1008.7", 
                        "rising": "1", 
                        "visibility": ""
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "62", 
                        "pressure": "1013.3", 
                        "rising": "0", 
                        "visibility": "16.09"
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "80", 
                        "pressure": "1017.7", 
                        "rising": "2", 
                        "visibility": "9.66"
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "93", 
                        "pressure": "1012.9", 
                        "rising": "2", 
                        "visibility": "8.05"
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "82", 
                        "pressure": "1016.8", 
                        "rising": "1", 
                        "visibility": ""
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "99", 
                        "pressure": "1015.92", 
                        "rising": "0", 
                        "visibility": "16.09"
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "89", 
                        "pressure": "982.05", 
                        "rising": "0", 
                        "visibility": "16.09"
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "88", 
                        "pressure": "1015.92", 
                        "rising": "0", 
                        "visibility": "16.09"
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "100", 
                        "pressure": "1015.92", 
                        "rising": "1", 
                        "visibility": "8.05"
                    }
                }, 
                {
                    "atmosphere": {
                        "humidity": "81", 
                        "pressure": "1015.5", 
                        "rising": "0", 
                        "visibility": "16.09"
                    }
                }
            ]
        }
    }
}

```

#### *Weather.get_current_wind(place)*
>Return weather wind

```python
data = weather.get_current_wind('Barcelona')
```

```json
{
    "query": {
        "count": 7, 
        "created": "2015-07-08T08:44:49Z", 
        "lang": "en-US", 
        "results": {
            "channel": [
                {
                    "wind": {
                        "chill": "27", 
                        "direction": "110", 
                        "speed": "14.48"
                    }
                }, 
                {
                    "wind": {
                        "chill": "15", 
                        "direction": "300", 
                        "speed": "24.14"
                    }
                }, 
                {
                    "wind": {
                        "chill": "23", 
                        "direction": "", 
                        "speed": ""
                    }
                }, 
                {
                    "wind": {
                        "chill": "22", 
                        "direction": "190", 
                        "speed": "9.66"
                    }
                }, 
                {
                    "wind": {
                        "chill": "31", 
                        "direction": "220", 
                        "speed": "17.7"
                    }
                }, 
                {
                    "wind": {
                        "chill": "17", 
                        "direction": "360", 
                        "speed": "12.87"
                    }
                }, 
                {
                    "wind": {
                        "chill": "26", 
                        "direction": "80", 
                        "speed": "28.97"
                    }
                }
            ]
        }
    }
}

```

#### *Weather.get_astronomy(place)*
>Return sunrise and sunset time

```python
data = weather.get_astronomy('Congo')
```

```json
{
    "query": {
        "count": 10, 
        "created": "2015-07-08T08:45:44Z", 
        "lang": "en-US", 
        "results": {
            "channel": [
                {
                    "astronomy": {
                        "sunrise": "6:10 am", 
                        "sunset": "6:11 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "7:07 am", 
                        "sunset": "4:58 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "6:03 am", 
                        "sunset": "6:41 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "5:38 am", 
                        "sunset": "8:32 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "5:55 am", 
                        "sunset": "8:27 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "5:55 am", 
                        "sunset": "5:30 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "5:38 am", 
                        "sunset": "5:20 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "6:05 am", 
                        "sunset": "8:57 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "5:36 am", 
                        "sunset": "7:57 pm"
                    }
                }, 
                {
                    "astronomy": {
                        "sunrise": "5:55 am", 
                        "sunset": "8:51 pm"
                    }
                }
            ]
        }
    }
}

```


