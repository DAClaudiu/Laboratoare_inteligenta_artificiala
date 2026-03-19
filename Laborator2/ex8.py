tari_risc = ["Coreea de Nord", "Siria", "Iran"]
tranzactii_suspecte_totale = 0
cont_activ = True

print("=== Sistem de Monitorizare Bancară ===")

while cont_activ:
    print(f"\n[Tranzacții suspecte detectate: {tranzactii_suspecte_totale}/3]")

    try:
        suma = float(input("Introduceți suma tranzacției (RON): "))
        tara = input("Introduceți țara de origine: ").strip()

        este_suspecta = False

        if tara in tari_risc:
            print(f"Tranzacție: {suma} RON din {tara} → FRAUDULOASĂ (Țară risc ridicat)")
            este_suspecta = True

        elif suma > 10000:
            print(f"Tranzacție: {suma} RON din {tara} → SUSPICIOASĂ (Sumă mare)")
            este_suspecta = True

        else:
            print(f"Tranzacție: {suma} RON din {tara} → Sigură")

        if este_suspecta:
            tranzactii_suspecte_totale += 1

        if tranzactii_suspecte_totale >= 3:
            print("\n" + "!" * 40)
            print("ALERTĂ: 3 tranzacții suspecte detectate!")
            print("CONT BLOCAT PENTRU SIGURANȚĂ.")
            print("!" * 40)
            cont_activ = False

    except ValueError:
        print("Eroare: Vă rugăm să introduceți o sumă numerică validă.")

    if cont_activ:
        continuare = input("\nProcesați altă tranzacție? (da/nu): ").lower()
        if continuare != 'da':
            break

print("\nSistemul s-a închis. Raport final generat.")