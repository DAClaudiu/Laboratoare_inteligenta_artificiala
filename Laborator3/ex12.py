dict1 = {i: i**2 for i in range(1,11)}
print(dict1)

text = "laborator"
dict2 = {char: text.count(char) for char in set(text)}
print(dict2)

dict3 = {x: [div for div in range(1,x+1) if x%div==0] for x in range(1,11)}
print(dict3)