import random


magic_number= random.randint(1,50)
incercari = 0

guessed_number = None
print("Am ales un numar intre 1 si 50. Ghiceste-l!")


while guessed_number != magic_number:
    guessed_number = int(input('Introdu un numar: '))
    incercari+=1

    if guessed_number > magic_number:
        print('Mai mic! Incearca din nou.')
    elif guessed_number < magic_number:
        print('Mai mare! Incearca din nou.')
    else:
        print(f'Felicitari! Ai ghicit numarul magic: {magic_number} in {incercari} incercari')
