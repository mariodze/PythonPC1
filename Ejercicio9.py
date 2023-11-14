'''

Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
'día', 'buen', 'Di'].


'''
lista= input('Ingresa elementos a la lista separados por una coma: \n')
nueva_lista=lista.split(',')
print(f'\n Ingresaste: \n {nueva_lista}')

#Para borrar espacios en blanco y elementos vacíos
elementos = [elemento.strip() for elemento in nueva_lista if elemento.strip()] 

if nueva_lista==elementos:  
  nueva_lista.reverse()
  print(f'la lista invertida es:\n {nueva_lista}')
else:
   print(f'Porfavor, evite ingresar espacios en blanco \n su lista sin errores sería: \n {elementos}')
   elementos.reverse()
   print(f'Lista invertida: \n {elementos}')


'''
si en el if pongo len(nueva_lista)==len(elementos): 
solo compararía respecto a la cantidad y si pongo un elemento con un monton de espacios?


Ingresa elementos a la lista separados por una coma: 
1,2,3,4,5, 6            ,7

 Ingresaste: 
 ['1', '2', '3', '4', '5', ' 6            ', '7']
la lista invertida es:
 ['7', ' 6            ', '5', '4', '3', '2', '1']

 por eso seria mejor compara elementos por elemento de cada una de las listas :
 if nueva_lista==elementos
 
'''


