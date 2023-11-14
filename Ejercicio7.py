'''
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.


'''


a= float(input('Ingrese el primer numero: '))
b= float(input('Ingrese el segundo numero: '))

print("MENU")
print(' 1. Mostrar una suma de los dos números \n 2. Mostrar una resta de los dos números (el primero menos el segundo) \n 3. Mostrar una multiplicación de los dos números \n 4. Salir')


opc= int(input('Ingrese el valor de la opcion: '))

    
if opc==1:
   suma=a+b
   print(f"La suma es: {suma}")

elif opc==2:
   resta=a-b
   print(f'La resta es: {resta}')

elif opc==3:
   multiplicacion=a*b
   print(f"La multiplicación es: {multiplicacion}")

elif opc==4:
   print('Saliendo del programa')
   
else:
   print('Error. Ingrese una opcion correcta')




'''
a = 0  
b = 0  

while True:
    if a ==0 and b==0:
        a = float(input('Ingrese el primer número: '))
        b = float(input('Ingrese el segundo número: '))

    print("MENU")
    print(' 1. Mostrar una suma de los dos números \n 2. Mostrar una resta de los dos números (el primero menos el segundo) \n 3. Mostrar una multiplicación de los dos números \n 4. Salir')

    opc = int(input('Ingrese el valor de la opción: '))

    if opc == 1:
        suma = a + b
        print(f"La suma es: {suma}")

    elif opc == 2:
        resta = a - b
        if resta >= 0:
            print(f"La resta es: {resta}")
        else:
            print(f'La resta es negativa: {resta}')

    elif opc == 3:
        multiplicacion = a * b
        print(f"La multiplicación es: {multiplicacion}")

    elif opc == 4:
        print('Saliendo del programa, volviendo al menú')
        break  # Sale del bucle si se selecciona la opción 4

    else:
        print("Error. Ingrese el valor de una de las opciones del menú: 1, 2, 3, 4")
   
'''


