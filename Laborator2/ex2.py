
grade = None

while (grade == None):
    user_input = input('Introdu nota: ')
    grade_value = int(user_input)


    if grade_value < 1 or grade_value > 10:
        print("Nota invalida! Te rog introdu o valoare intre 1 si 10.")
        grade = None
    else:
        grade = grade_value


if (grade>=9 and grade<=10):
    print('Excelent')
elif (grade>=7 and grade<=8):
    print('Bine')
elif (grade>=5 and grade<=6):
    print('Suficient')
elif (grade<5):
    print('Reexaminare')
