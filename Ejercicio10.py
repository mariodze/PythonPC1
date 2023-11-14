'''

Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']


'''
lista= input('Ingrese 6 o mas elementos a la lista separados por una coma: \n')
nueva_lista=lista.split(',')

#para saber cuantos elementos tiene la lista
cantidad= len(nueva_lista)

#Para borrar espacios en blanco y elementos vacíos
elementos = [elemento.strip() for elemento in nueva_lista if elemento.strip()] 

if cantidad>=6:
     if nueva_lista==elementos:  
      print(f'\n Lista ingresada sin errores: \n {nueva_lista}')
      nueva_lista.remove(nueva_lista[5])
      nueva_lista.remove(nueva_lista[4])
      nueva_lista.remove(nueva_lista[0])
      print(f'\n La Nueva lista con elementos eliminados en posicion 0,4,5 \n {nueva_lista}')
     else:
      print(f'\n Porfavor, evite ingresar espacios en blanco y elementos vacios \n Su lista sin errores sería: \n {elementos}')
      elementos.remove(elementos[5])
      elementos.remove(elementos[4])
      elementos.remove(elementos[0])
      print(f'\n La Nueva lista con elementos eliminados en posicion 0,4,5 es: \n {elementos}')

else:
     if nueva_lista==elementos:
       print('Ingrese 6 o mas elementos')
     else:
       print('Ingrese 6 o mas elementos y en el formato correcto(sin espacios ni elementos vacios)')






'''
lista= input('Ingrese 6 o mas elementos a la lista separados por una coma: \n')
nueva_lista=lista.split(',')

#para saber cuantos elementos tiene la lista
cantidad= len(nueva_lista)

#Para borrar espacios en blanco y elementos vacíos
elementos = [elemento.strip() for elemento in nueva_lista if elemento.strip()] 

if cantidad>=6 and nueva_lista==elementos:  
   nueva_lista.remove(nueva_lista[5])
   nueva_lista.remove(nueva_lista[4])
   nueva_lista.remove(nueva_lista[0])
   print(f'\n La Nueva lista con elementos eliminados en posicion 0,4,5 \n {nueva_lista}')

elif 1<=cantidad<6 and nueva_lista==elementos:
      print('Ingrese 6 o mas elementos')
elif 1<=cantidad<6 and nueva_lista!=elementos:
     print('Ingrese 6 o mas elementos y en el formato correcto(sin espacios ni elementos vacios)')
elif cantidad>=6 and nueva_lista!=elementos:
     print(f'Porfavor, evite ingresar espacios en blanco \n su lista sin errores sería: \n {elementos}')
     elementos.remove(elementos[5])
     elementos.remove(elementos[4])
     elementos.remove(elementos[0])
     print(f'\n La Nueva lista con elementos eliminados en posicion 0,4,5 \n {elementos}')



'''
