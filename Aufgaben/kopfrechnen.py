import random

operatoren = ['+', '-', '*', '/']

def aufgabe_generieren():
    num_1 = random.randint(1,10)
    num_2 = random.randint(1,10)
    input_operator = input("Wähle einen Operator (+, -, *, /): ")
    if input_operator not in operatoren:
        print('Ungültiger Operator. Bitte wähle einen der folgenden Operatoren: +, -, *, /')
        aufgabe_generieren()
    if input_operator == '+':
        aufgabe = f'{num_1} + {num_2}'
        ergebnis = num_1 + num_2
    elif input_operator == '-':
        aufgabe = f'{num_1} - {num_2}'
        ergebnis = num_1 - num_2
    elif input_operator == '*':
        aufgabe = f'{num_1} * {num_2}'
        ergebnis = num_1 * num_2
    else:
        aufgabe = f'{num_1} / {num_2}'
        ergebnis = num_1 // num_2
    return aufgabe, ergebnis, input_operator
    

def main():
    gesamt_fragen = 5
    versuchen_anzahl = 5
    richtige_antworten = 0
    print(f'Let`s get it Started!')
    for _ in range(gesamt_fragen):
        aufgabe, ergebnis, input_operator = aufgabe_generieren()
        if versuchen_anzahl == 1:
            print(f'Du hast ein lezter Versuch \n {aufgabe}')
        else:
            print(f'Du hast noch {versuchen_anzahl} Versuchen \n {aufgabe}')
        if input_operator == '/':
            print("Gib bitte nur den ganzen Teil ein")
        input_ergebnis = int(input('Antwort: '))
        if input_ergebnis == ergebnis:
            print(f'Deine Antwort ist {input_ergebnis}, und das ist richtig!')
            versuchen_anzahl -= 1
            richtige_antworten += 1
        else:

            print(f'Deine Antwort ist {input_ergebnis}, und das ist leider falsh, richtige Antwort is {ergebnis}')
            versuchen_anzahl -= 1
    print(f'Du hast auf {richtige_antworten} von {gesamt_fragen} Fragen richtig geantwortet')


if __name__ == "__main__":
    main()