list1 = [x for x in range(101) if x % 2 == 0]
print(list1)

list2 = [x**3 for x in range(11)]
print(list2)

list3 = [1,2,3,4,5]
list4 = [4,5,6,7,8]
list5= [x for x in list3 if x in list4]
print(list5)