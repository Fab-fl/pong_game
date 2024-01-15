import time
def Rechner():
    zahl1 = input('gib Zahl 1 ein:')
    zahl2 = input('gib Zahl 2 ein:')
    operator = input('bitte gib deinen Rechenoperator ein (+/-/*/:)')
    result = 0
    if operator == '+':
        result = int(zahl1) + int(zahl2)
        print(result)
        time.sleep(2)
    elif operator == '-':
        result = int(zahl1) - int(zahl2)
        print(result)
        time.sleep(2)
    elif operator == '*':
        result = int(zahl1) * int(zahl2)
        print(result)
        time.sleep(2)
    elif operator == ':':
        result = int(zahl1) / int(zahl2)
        print(result)
        time.sleep(2)
    else: 
        print('etwas ist schief gelaufen')
        time.sleep(2)
    Rechner()

Rechner()
