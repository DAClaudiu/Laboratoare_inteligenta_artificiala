set1 = {x for x in range(21) if x%2==0}
print(set1)

cuvant = "facultate"
set2 = {char for char in cuvant if char.isalpha()}
print(set2)

propozitie = "The quick brown fox jumps over the lazy dog"
set3 = {word for word in propozitie.split() if len(word) >= 5}
print(set3)