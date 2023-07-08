#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 19:32:03 2023

@author: Tulayev Izzat
"""
import request
import json

wikiurl = "https://www.mediawiki.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=2"
response = request.get(wikiurl)

print(json.dumps(response.json()), indent=True)