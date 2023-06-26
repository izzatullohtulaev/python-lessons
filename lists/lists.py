# radius = 10
# name = "Boyka"

fruits = ["olma", "anjir", "shaftoli", "o'rik"]
prices = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
numbers = ['bir', 'ikki', 'uch', 4, 5]
names = []

# print("First fruit of the list:", fruits[0])
# print("Last fruit of the list:", fruits[-1])

# --------Special methods---------------------
fruits.append('xolit')

cars = []
cars.append('Lacetti')
cars.append('Nexia 3')
cars.append('Cobalt')
cars.insert(3, 'malibu')
del cars[0]
# print(cars)

animals = ['dog', 'cat', 'cow', 'sheep', 'rabbit', 'cat']
animals.remove('cat')

shopping = ['oil', 'meat', 'banana', 'onion', 'potato', 'tomato']
bought = shopping.pop(3)
print(f"I bought {bought} from Makro and removed from the shopping list")
print("Things that haven't bought :", shopping)
print("Shut up")