d = {"a": 123, "b": 234, "c": 345, "d": 456, "e": 678}

"""
Gegeben ist obiges Dictionary.

1. Füge ein neues Item (Schlüssel-Wert-Paar) hinzu: Schlüssel ist ein String, Wert ein Integer
2. Füge ein neues Item hinzu: Schlüssel ist ein String, Wert ein beliebige Liste (z.B. [1,2,3])
3. Indiziere ein beliebiges Element aus der hinzugefügten Liste.
4. Füge ein neues Item hinzu: Schlüssel ist ein String, Wert ein beliebiges Dictionary.
5. Indiziere einen beliebigen Wert aus dem hinzugefügten Dictionary.
6. Iteriere per Schleife über die Schlüssel und gebe sie aus.
7. Iteriere per Schleife über die Werte und gebe sie aus.
"""
#######
d['f'] = 999
#######
d['list'] = [1,2,3]
#######
print(d['list'][0])
#######
d['dict'] = {"key1":1, "key2":2}
#######
print(d["dict"]["key1"])

for key in d.keys():
    print(key)
#######
for v in d.values():
    print(v)


"""
Erstelle ein neues dictionary in dem Schlüssel und Werte aus d vertauscht sind.
Per Schleife und leerem dictionary.
Oder per dictionary comprehension.
"""

# d_new = {}
# for ... in d.items():
#     d_new[...] = ...

########

# d_new = {..... for .... in d...}


# Frage: Was passiert beim Vertauschen, falls die Werte in d Dictionary nicht eindeutig sind,
# es Duplikate gibt?