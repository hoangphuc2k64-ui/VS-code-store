items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']

print(items.index('Python'))     # 0
print(items.index('Python', 1))  # 5
# print(items.index('Java', 3))    # ValueError: 'Java' is not in list

print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0

# =================================================
items1 = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items1.sort()
print(items1)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items1.reverse()
print(items1)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']