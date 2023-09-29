"""
Öffne eine Datei text.txt
Schreibe drei Zeilen hinein.
"""

with open("text.txt", "w") as f:
    f.write("Zeile1\n")
    f.write("Zeile2\n")
    f.write("Zeile3")

"""
Öffne die selbe Datei.
1. Lese alle Zeilen auf einmal aus.
2. Schließen und nochmal öffnen. Nun lies jede Zeile gesondert aus.
"""

with open("text.txt", "r") as f:
    print(f.readlines())

with open("text.txt", "r") as f:
    print(f.readline(10))
    print(f.readline(10))
    print(f.readline(10))

"""
Öffne die selbe Datei. Achte auf den korrekten file-Modus beim Öffnen, lesen und schreiben!
1. Lese alle Zeilen auf einmal aus.
2. Setze den file pointer auf den Anfang der zweiten Zeile
3. Überschreibe nur genau die zweite Zeile (nicht den Rest)
"""

with open("text.txt", "r+") as f:
    print(f.readlines())
    f.seek(7, 0)
    f.write("blabla\n")

with open("text.txt", "r") as f:
    print(f.readlines())
