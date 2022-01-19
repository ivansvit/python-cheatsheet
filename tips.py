# 1. Iterate with enumerate() instead of range(len())

data = [1, 3, -9, -10, 4]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0
print(data)

data = [1, 3, -9, -10, 4]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0
print(data)

# 2. Use list comprehension instead of for raw loop
squares = []
for i in range(10):
    squares.append(i * i)
print(squares)

squares = [i*i for i in range(10)]
print(squares)

# 3. Sort complex iterables with sorted()
data = (3, 5, 6, 3, 1, 10)
sorted_data = sorted(data, reverse=True)
print(sorted_data)

data = [{"name": "Leo", "age": 2},
        {"name": "Cri", "age": 20},
        {"name": "Mikki", "age": 10}]
sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)

# 4. Store unique values with sets.
my_list = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7]
my_set = set(my_list)
print(my_set)

primes = {2, 3, 5, 7, 11, 13, 17, 23}
print(primes)

# 5. Save memory with generators
import sys
my_list = [i for i in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")

# 6. Define default values in Dictionaries with .get() and .setdefault()
my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count", 0)
print(count)

count = my_dict.setdefault("count", 1)
print(count)
print(my_dict)

# 7. Count hashable objects with collections.Counter
from collections import Counter

my_list = [1,1,1,1,3,4,4,5,5,6,6,6,7,7]
counter = Counter(my_list)
print(counter)
most_common = counter.most_common(2)
print(most_common)

# 8. Concat string with .join()
list_of_strings = ["Leo", "jumps", "all", "day", 0]
my_string = " ".join(str(item) for item in list_of_strings)
print(my_string)

# 9. Merge 2 dict
d1 = {"name": "Ale", "age": 30}
d2 = {"name": "Ale", "city": "Montalto"}
d3 = {"name": "Cris", "age": 40}
merged_dict = {**d1, **d2} # Python 3.5
merged_dict2 = d1 | d2 # Python 3.9
print(merged_dict2)

# 10. Simplify if statement for multiple checks
colors = ["red", "green", "blue"]
c = "red"
if c in colors:
    print("Is main color.")