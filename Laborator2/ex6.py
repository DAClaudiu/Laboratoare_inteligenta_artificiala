inventar = []
joc_activ = True

print("=== AVENTURA IN TARAMUL DIN NEANT ===")
print("Te afli la o rascruce de drumuri. Esti gata de aventura?")

while joc_activ:
    print("\nDirectii: [stanga] (Muntele) sau [dreapta] (Raul)")
    pas1 = input("Incotro? ").lower()

    if pas1 == "stanga":
        print("\nAjungi la poalele muntelui. Ai de ales intre [grota] sau [carare].")
        pas2 = input("Alegerea ta: ").lower()

        if pas2 == "grota":
            print("Intri in grota si gasesti o SABIE DE ARGINT!")
            if "Sabie de Argint" not in inventar:
                inventar.append("Sabie de Argint")
        elif pas2 == "carare":
            print("Urcand pe carare, intalnesti un LUP!")
            if "Sabie de Argint" in inventar:
                print("Lupul vede sabia ta si se sperie. Ai trecut cu bine!")
            else:
                print("Lupul te ataca! Ai fugit inapoi cu coada intre picioare.")
        else:
            print("Te-ai ratacit printre stanci.")

    elif pas1 == "dreapta":
        print("\nAjungi la rau. Poti merge spre [cascada] sau spre [pod].")
        pas2 = input("Alegerea ta: ").lower()

        if pas2 == "cascada":
            print("In spatele cascadei gasesti o AMULETA MAGICA!")
            if "Amuleta Magica" not in inventar:
                inventar.append("Amuleta Magica")
        elif pas2 == "pod":
            print("Pe pod te opreste un Troll. Iti cere Amuleta pentru a te lasa sa treci.")

            if "Amuleta Magica" in inventar:
                print("Ii dai Amuleta. Troll-ul te lasa sa treci si primesti o HARTA!")

                inventar.remove("Amuleta Magica")
                inventar.append("Harta")

            else:
                print("Nu ai Amuleta. Troll-ul te impinge in apa!")

        else:
            print("Ai cazut in rau si te-ai udat tot.")

    else:
        print("Directie invalida. Te-ai intors la inceput.")
        continue

    print(f"\nInventarul tau: {inventar}")
    raspuns = input("\nMai continui aventura? (da/nu): ")
    if raspuns.lower() != "da":
        joc_activ = False

print("\n--- SFARSITUL AVENTURII ---")
print(f"Obiecte finale: {inventar}")
