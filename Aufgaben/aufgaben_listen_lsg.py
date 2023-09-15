import random

# nums = list(range(10))
# l = [random.choice(nums) for _ in range(100)]
# print(l)
# l = []
# for _ in range(100):
#     l.append(random.choice(nums))
# print(l)

"""
Gegeben ist obige Liste.
1. Sortiere aufsteigend
2. Zähle die Zahl 6
3. Erstelle eine neue Liste aus jedem 3. Element der Liste
4. Erstelle eine Liste aus jedem 2 Element, angefangen von Index 50
5. ... eine Liste aus jedem zweiten Element in umgekehrter Reihenfolge
"""

# l_sort = sorted(l)
# print(l_sort)
# num_6 = l.count(6)
# print(num_6)
# l_new = l[::3]
# print(l_new)
# l_new = l[50::2]
# print(l_new)
# l_new = l[::-2]
# print(l_new)

"""
Erstelle eine verschachtelte Liste aus: Drei Listen mit jeweils 10 Integerzahlen.
Benutze eine Schleife in einer Schleife, um alle gerade Zahlen in einer neuen Liste zu sammeln.
"""

# l_nested = [list(range(10)), list(range(10)), list(range(10))]
# print(l_nested)
# l_even = []
# for l in l_nested:
#     print(f"list {l}")
#     for n in l:
#         print(f"num {n}")
#         if n % 2 == 0:
#             l_even.append(n)

"""
Erstelle eine Liste eine Liste aus Zahlen bis 10000, die durch 2 und 3 teilbar sind
"""

# l_new = [n for n in range(10) if n % 2 == 0 and n % 3 == 0]
# print(l_new)

"""
Gegeben ist folgende Liste divisors
Erstelle eine Liste eine Liste aus Zahlen bis 50000, die durch die Zahlen in der Liste teilbar sind.
Verwende, wenn möglich, eine nested list comprehension
"""

# divisors = [2, 3, 7, 11]

# nums = [i for i in range(50000) for divisor in divisors if i % divisor == 0]
# print(nums)

"""
Bonus:
Wähle per list comprehension die Wörter, deren Buchstaben alle in chars vorkommen.
"""

# chars = "anptherg"
# words = ["zoo", "xylophon", "anna", "panther", "garage"]

# l = [
#     word
#     for word in words
#     if [True if char in chars else False for char in word].count(False) == 0
# ]
# print(l)

# #####
# l = []
# for word in words:
#     all_chars_in = True
#     for char in word:
#         if char not in chars:
#             all_chars_in = False
#     if all_chars_in:
#         l.append(word)

# print(l)


s = "this is a string"
s = s.split(" ")
print(",".join(s))

