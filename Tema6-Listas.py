lista1 = ["Juan", 1,2,23,True]

print(lista1)

print(lista1[2:4])
print(lista1[:2])
print(lista1[3:])
lista1.append("Cleto")
print(lista1)
lista1.insert(0, "Isabel")
print(lista1)


lista1.extend([9,10,11])
print(lista1)
print(lista1.index("Cleto"))
lista1.remove("Juan")
print(lista1)
lista1.pop()
print(lista1)