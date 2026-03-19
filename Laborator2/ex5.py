import random

numere_loterie = []


while len(numere_loterie) < 6:
    numar = random.randint(1, 49)
    if numar not in numere_loterie:
        numere_loterie.append(numar)
print('Bine ai venit la Loteria Python! ')
print('Alege 6 numere intre 1 si 49.')

numere_ghicite = []
index = 1

while len(numere_ghicite) < 6 :
    print('Numarul', index, end='')
    numar = int(input(': '))

    if (numar not in numere_ghicite) and (numar>0 and numar<=49):
        numere_ghicite.append(numar)
        index += 1

print('Numere extrase:', numere_loterie)
numere_ghicite_corect = 0
for i in numere_ghicite:
    if i in numere_loterie:
        numere_ghicite_corect += 1

print('Ai ghicit', numere_ghicite_corect, 'numere: ', end='' )
for i in numere_ghicite:
    if i in numere_loterie:
        print(i,',', end='')

if (numere_ghicite_corect == 0):
    print('Nu ai castigat nimic!')
elif (numere_ghicite_corect>=1 and numere_ghicite_corect <=3):
    print('Felicitari! Ai castigat un premiu mic.')
elif (numere_ghicite_corect>=4 and numere_ghicite_corect <=5):
    print('Felicitari! Ai castigat un premiu mare.')
elif (numere_ghicite_corect==6):
    print('Felicitari! Ai castigat Jackpot-ul')
