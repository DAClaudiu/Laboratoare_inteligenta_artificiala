cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urat", "prost", "groaznic", "dezamagitor"]

comentariu = input("Introdu comentariul tau: ").lower()

este_pozitiv = False
este_negativ = False

for cuvant in cuvinte_pozitive:
    if cuvant in comentariu:
        este_pozitiv = True
        break

for cuvant in cuvinte_negative:
    if cuvant in comentariu:
        este_negativ = True
        break

if este_pozitiv and not este_negativ:
    print("Comentariu pozitiv!")
elif este_negativ and not este_pozitiv:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")
