''' 
Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

'''

num_show= int(input ('Ingresar cantidad de show vistos en el ultimo año: '))

valor_verdad = 3<num_show  #guardamos el resultado True-False n una variable de tipo booleana
print(f'\n¿Ha visto más de 3 shows musicales en el último año?\n {valor_verdad}')