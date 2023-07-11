import re
import uzwords
import apikey

word_array = [
    "apple", "banana", "carrot", "dog", "elephant", "fox", "grape", "horse", "ice cream", "jellyfish",
    "kangaroo", "lemon", "mango", "nut", "orange", "peach", "quail", "rabbit", "strawberry", "turtle",
    "unicorn", "violet", "watermelon", "xylophone", "yak", "zebra", "ant", "bee", "cat", "duck",
    "egg", "fish", "giraffe", "hamster", "iguana", "jaguar", "kiwi", "lion", "monkey", "newt",
    "octopus", "penguin", "quokka", "rhino", "sheep", "tiger", "umbrella", "vulture", "walrus", "x-ray",
    "yoyo", "zeppelin", "almond", "broccoli", "cucumber", "dragonfruit", "eggplant", "fig", "grapefruit", "hazelnut",
    "jackfruit", "kale", "leek", "mushroom", "nectarine", "olive", "papaya", "quince", "radish", "spinach",
    "tomato", "ugli fruit", "vanilla", "watercress", "xigua", "yam", "zucchini", "avocado", "blueberry", "cherry",
    "date", "elderberry", "fig", "ginger", "honeydew", "imbe", "jujube", "kiwifruit", "lime", "mango",
    "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla", "watermelon"
]


word1 = "темир"
word2 = "такир"
word3 = "тулпор"

andoza = "^т...р$"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

matches = []
andoza = "^т...р$"
for word in uzwords.words:
    if re.match(andoza, word):
        matches.append(word)
# print(matches)


andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
email = re.findall(andoza, matn)