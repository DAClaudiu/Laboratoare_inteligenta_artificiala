lista_preturi = [10, 50, None, 7, None, 35, 99, None]

fara_none = list(filter(lambda x: x is not None, lista_preturi))

lista_preturi_actualizata = list(map(lambda x: round(x * 0.9,2), fara_none))

print(lista_preturi_actualizata)