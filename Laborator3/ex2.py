def genereaza_factura(nume_client, **kwargs):
    print("=== FACTURA ===")
    print(f"Client: {nume_client}")

    total = 0

    for produs, pret in kwargs.items():
        print(f"{produs}: {pret} lei")
        total += pret

    print(f"Total: {total} lei")


genereaza_factura(
    "Andrei Popescu",
    paine=5,
    lapte=8,
    oua=12
)