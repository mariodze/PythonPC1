'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

'''

edad= int(input("Indique su edad en años: "))

if 0<=edad<4:
    precio=0
    print(f'El monto a pagar es ${precio} ')
    
elif 4<=edad<=18:
    precio=5
    print(f'El monto a pagar es ${precio} ')

elif edad>18:
    precio=10
    print(f'El monto a pagar es ${precio} ')
else:
    print("Error ingrese un valor correcto")


