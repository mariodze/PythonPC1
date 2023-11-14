''' 

En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.

Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.

'''

while True: #para crear un bucle infinito por si el usuario ingresa mal el porcentaje

    consumo = float(input("Ingrese el precio total consumido en $: "))
    porcentaje_num = float(input("Ingrese porcentaje de propina igual o superior a 15% : "))
    porcentaje_dec = porcentaje_num / 100

    if 15 <= porcentaje_num:

        propina = porcentaje_dec * consumo
        total=propina+consumo
        print(f'\n El precio de la propina es: {propina:.2f} $\n El total incluido propina es: {total:.2f} $')
        break  # Sale del bucle si la entrada es válida

    else:
        print(f'\n Valor incorrecto, ingrese un valor superior al 15%. Intente de nuevo.')
   

