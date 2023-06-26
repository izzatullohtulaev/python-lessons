# # Sorting
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi'];
# cars.sort()
# print(cars)

# # Reverse-Sorting
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi'];
# print(cars)
# cars.sort(reverse=True )
# print(cars)

# SORTED()
guests = ['Boyka', 'Milana', 'JJ', 'Belka', 'Mita']
# print("SORTED() funksiyasi qaytargan ro'yxat:", sorted(guests))
# print("Ro'yxat o'zgarmay qoldi:", guests)
# print("Teskari tartib:", sorted(guests, reverse=True))

# .reverse()
fruits = ['pear', 'banana', 'apple', 'cherry', 'watermelon', 'lemon']
fruits.reverse()
# print(fruits)

# LEN()
numbers = [34, 23, 12.21, 45, 56, 43]
# print(len(numbers))

# RANGE() and steps
# Example: list_name = list(range(starting_number*, ending_number*, steps))
evens = list(range(0, 21, 2))
odds = list(range(1,21, 2))
# print('Evens:', evens)
# print('Odds:', odds)

# MIN(), MAX(), SUM()
prices = [12000, 21000, 5600, 23000, 1200, 43000, 86000]
low_price = min(prices)
high_price = max(prices)
total_price = sum(prices)
# print("Lowest price:", low_price)
# print("Highest price:", high_price)
# print("Total:", total_price)

# Snipping the list
fruits = ['pear', 'banana', 'apple', 'cherry', 'watermelon', 'lemon']
pba = fruits[0:3] # PBA - Pear, Banana, Apple😁
cwl = fruits[3:6] # CWL - Cherry, Watermelon, Lemon😁
# print("PBA:", pba)
# print("CWL:", cwl)

# Copying the list to another one
fruits = ['pear', 'banana', 'apple', 'cherry', 'watermelon', 'lemon']
duplicated_list = fruits[:]
duplicated_list.append('melon')
duplicated_list.append('pineapple')
# print("fruits list:", fruits)
# print("duplicated_list list:", duplicated_list)

# Tuples
toys = ('bus', 'car', 'dino', 'bear', 'lizard', 'cow', 'snake')
# toys[3] = 'dragon' ❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌

# Tuples <-> List
toys = ('bus', 'car', 'dino', 'bear', 'lizard', 'cow', 'snake')
toys = list(toys)
toys[3] = 'dragon'
print(toys)