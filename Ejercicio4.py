''' 

Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma:

        1+2+3+...n = n(n+1)/2

'''

numero= int (input('Ingrese un numero entero positivo: '))

if numero>0:

 suma=numero*(numero+1)/2
 print(f'La suma de los N= {numero} primeros numeros es {suma:.0f}')

elif numero==0:
 print('Error, ingrese un valor superior')

else:
  print('Error, ingrese un valor positivo')

   