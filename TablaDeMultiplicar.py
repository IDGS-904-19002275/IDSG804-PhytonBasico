def multiplicar (num):
    for i in  range(1,11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")

numero = int (input("Ingresa el numero que quieres multiplicar "))
multiplicar(numero)