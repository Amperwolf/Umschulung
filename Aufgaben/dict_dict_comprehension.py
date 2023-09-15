d = {"key1": 1, "key2": 2, "key3": 3}

# Indizierung über Schlüssel
print(d["key1"])
d["key1"] = "new value"
d["key1"] = 1

print(d.items())
print(d.keys())
print(d.values())

for key, val in d.items():
    print(f"key: {key}, value: {val}")

sorted(d)
len(d)
list(reversed(d))
del d["key1"]


"""
Comprehension
"""

nums = list(range(10))
s = "abcdefgehi"

print(list(zip(nums, s)))

d = {key: val for key, val in zip(nums, s)}
print(d)
