reguli = {
    "piatra": "foarfeca",
    "foarfeca": "hartie",
    "hartie": "piatra"
}

def citeste_miscare(jucator):
    while True:
        try:
            alegere = input(f"Jucator {jucator}, ce alegi? ").lower()
            return alegere
        except ValueError:
            print("Alegere invalida! Incearca din nou.")


joc_nou = True

while joc_nou:
    m1 = citeste_miscare(1)
    m2 = citeste_miscare(2)

    if m1 == m2:
        print("Remiza")
    elif reguli[m1] == m2:
        print("Jucatorul 1 castiga!")
    else:
        print("Jucatorul 2 castiga!")

    decizie = input("Doriti sa incepeti un joc nou? Y/N").strip()
    if decizie.lower() == "y":
        joc_nou = True
    elif decizie.lower() == "n":
        joc_nou = False
    else:
        print("Raspundeti cu Y/N.")