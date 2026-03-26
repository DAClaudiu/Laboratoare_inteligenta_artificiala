my_list = [1,2,3,4,5,6,7,8,9,10]

square = lambda x: x * x

result = list(map(square, my_list))
print(result)