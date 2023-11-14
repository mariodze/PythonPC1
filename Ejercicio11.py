'''

Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
lista. Su programa debe retornar otra lista sin los duplicados.
Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
Lista procesada: [1, 2, 3, 4,, 5]



'''

lista_ingresada = input(f'Ingrese elementos a la lista separados por una coma: \n')
lista=lista_ingresada.split(',')

#convertimos a cojunto la lista para eliminar elementos duplicados sin embargo esto no lo pone en el orden original de 'lista'
conjunto = set(lista)

#Convertimos el conjunto a lista con el orden inicial de la lista , con la funcion sorted
nueva_lista= sorted(conjunto, key=lista.index)


#Se creo la lista nueva_elementos donde se almacenara los elementos de nueva_lista pero eliminando espacios en blanco y elementos vacíos si es que los hubiera, si no hubiera esos errores las dos listas serian practicamente lo mismo
nueva_elementos = [n_elemento.strip() for n_elemento in nueva_lista if n_elemento.strip()] 

#Se creo la lista elementos donde se almacenara los elementos de 'lista' pero eliminando espacios en blanco y elementos vacíos si es que los hubiera, si no hubiera esos errores las dos listas serian practicamente lo mismo
elementos = [elemento.strip() for elemento in lista if elemento.strip()] 

if nueva_lista==nueva_elementos:  
     print(f'Lista ingresada: \n {lista}')
     print (f'Lista sin elementos duplicados: \n {nueva_lista}')
else:
   if len(nueva_elementos)>0:
     print (f'\n Porfavor, evite ingresar espacios en blanco y elementos vacios \n La lista ingresada sin espacios ni elementos vacios seria: \n {elementos}')
     print(f'\n La lista final sin duplicados es: \n {nueva_elementos}')
   else:
      print('Error. Porfavor ingrese un elemento a la lista')





'''
La función sorted() en Python se utiliza para ordenar elementos de una iterable (como una lista,tupla,conjunto) en un nuevo iterable, 
ya sea ascendente o descendente. La función toma la forma general:

sorted(iterable, key=key, reverse=reverse)


-iterable: La secuencia que deseas ordenar, lista,tupla,conjunto
-key (opcional): Una función que toma un elemento y devuelve un valor que se utilizará para la comparación durante la ordenación. Por defecto, utiliza el orden natural de los elementos.
-reverse (opcional): Un booleano que indica si la ordenación debe ser ascendente (False) o descendente (True). Por defecto, es False.

'''