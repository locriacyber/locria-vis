#!/usr/bin/env python
"""CNN weather forecast utility"""

import aiohttp
from urllib.parse import quote_plus as urlencode
from typing import List, Dict, Optional
from dataclasses import dataclass
from dacite import from_dict
from datetime import time, datetime

async def get_json(uri: str):
    async with aiohttp.request('GET', uri) as resp:
        return await resp.json()

@dataclass
class CurrentWeather:
    lastUpdated: datetime
    sunriseTime: time
    sunsetTime: time
    description: str
    temperature: int
    feelsLikeTemperature: int
    humidity: int
    dewPoint: int
    visibility: int
    wind: str

async def current_weather(latitude: float, longitude: float, *, locale='fahrenheit') -> CurrentWeather:
    res = await get_json(f'https://data.api.cnn.io/weather/getForecast/{latitude},{longitude}/{locale}')
    res = res['currentConditions']
    # TODO count timezoneOffset
    assert res['valid']
    t = res['lastUpdated']
    res['lastUpdated'] = datetime(t['year'], t['month'], t['day'], t['hours'], t['minutes'], t['seconds'])
    t = res['sunriseTime']
    res['sunriseTime'] = time(t['hours'], t['minutes'], t['seconds'])
    t = res['sunsetTime']
    res['sunsetTime'] = time(t['hours'], t['minutes'], t['seconds'])
    return from_dict(CurrentWeather, res)

@dataclass
class Place:
    latitude: float
    longitude: float
    continent: str
    country: str
    state: Optional[str]
    county: Optional[str]
    city: Optional[str]
    zipcode: Optional[str]
    asn_id: int
    asn_name: str
    ip_address: str

async def whereami() -> Place:
    res = await get_json("https://geo.ngtv.io/locate")
    res['asn_id'] = int(res['asn']['id'])
    res['asn_name'] = res['asn']['name']
    res['latitude'] = float(res['lat'])
    res['longitude'] = float(res['lon'])
    def first_or_none(o):
        if len(o) > 0:
            return o[0]
        else:
            return None
    location = first_or_none(res['states'])
    if location:
        res['state'] = location['state']
        res['county'] = first_or_none(location['counties'])
        res['city'] = first_or_none(location['cities'])
        res['zipcode'] = first_or_none(location['zipcodes'])
    return from_dict(Place, res)

async def main():
    """Get current weather here"""
    here = await whereami()
    weather = await current_weather(here.latitude, here.longitude)
    coords = f"{here.latitude},{here.longitude}"
    place = f"{here.continent} {here.country} {here.state or '-'} {here.county or '-'} {here.city or '-'} {here.zipcode or '-'}"
    as_ = f"ASN{here.asn_id} ({here.asn_name})"
    print(f"I'm currently at {coords}, or {place}.")
    print(f"In other words, {here.ip_address} at {as_}.")
    print(f"The weather here is {weather.description.casefold()}, at {weather.temperature}°F {weather.humidity}% with wind blowing at {weather.wind} and visibility of {weather.visibility}ppm.") # I think it's ppm
    print("It's a nice day to be alive!")
    print("Here's the chart you want:")
    keys = ["Geo Coordinates", "Name of Location", "IP Address", "Autonomous System", "Temperature", "Humidity", "Wind", "Visibility"]
    values = [coords, place, here.ip_address, as_, f"{weather.temperature}°F", f"{weather.humidity}%", weather.wind, f"{weather.visibility}ppm"]
    from tabulate import tabulate
    print(tabulate(zip(keys, values), tablefmt="rst"))

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
