from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from uzwords import words

# print(fuzz.ratio("olam", 'olma'))

text = "лала"
matches = process.extract(text, words, limit=3)