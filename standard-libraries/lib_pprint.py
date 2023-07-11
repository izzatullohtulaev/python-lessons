from pprint import pprint
import json

with open('bemor.json') as file:
    bemor = json.load(file)
bemor1 = str(bemor).replace('\n', '')
print(bemor)
pprint(bemor)