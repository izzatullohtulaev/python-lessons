#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 17:32:26 2023

@author: Tulayev Izzat
"""
import json
import googlemaps
from apikey import APIKEY

# GoogleMaps
gmaps = googlemaps.Client(key=APIKEY)
data = gmaps.geocode("Olmazor, Tashkent, Uzbekistan")

g = json.dumps(data[0], indent=4, sort_keys=True)
print(g)
