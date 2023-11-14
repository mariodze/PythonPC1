'''
La mayoría de los archivos tienen extensiones de archivo, el cual es un sufijo que comienza con un
punto (.) al final de su nombre. Por ejemplo, los nombres de archivo para GIF terminan en .gif y los
nombres de archivo para JPEG terminan en .jpg o .jpeg. Mientras que en los sistemas operativos
como Windows, el tipo de archivo le sirve al computador abrir el archivo en el formato apropiado, en
la web esto es distinto. Los navegadores web, por el contrario, se basan en tipos de medios,
anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en
la web.
Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
importar el uso de mayúsculas y minúsculas) :

- .gif                 image/gif
- .jpg                 image/jpeg
- .jpeg                image/jpeg 
- .png                 image/png
- .pdf                 application/pdf 
- .txt                 text/plain     
- .zip                 application/zip

Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.


Ejemplos:
Nombre Archivo: happy.jpg Salida Esperada: image/jpeg
Nombre Archivo: document.pdf Salida Esperada: application/pdf

Nota:
- El empleo de diccionarios podría ayudar con esta tarea.
- El uso de métodos de cadena sería muy útil al momento de separar el nombre del archivo de
su extensión.
'''


nombre_archivo = input('Ingrese el nombre de su archivo: \n')

if '.' in nombre_archivo:
     
     nombre, tipo=nombre_archivo.split('.')
     tipo_minuscula=tipo.lower()

     diccionario = {'jpg': 'image/jpeg' , 'gif' : 'image/gif', 'jpeg':'image/jpeg', 'png':'image/png', 'pdf': 'application/pdf', 'txt':'text/plain', 'zip':'application/zip'}

     if tipo_minuscula in diccionario:

        if tipo_minuscula=='gif':
            
            a=diccionario['gif']
            print(f'Su archivo es un MIME de tipo:\n {a}')

        elif tipo_minuscula=='jpg':
            b=diccionario['jpg']
            print(f'Su archivo es un MIME de tipo:\n {b}')

        elif tipo_minuscula=='jpge':
            c=diccionario['jpge']
            print(f'Su archivo es un MIME de tipo:\n {c}')
                
        elif tipo_minuscula=='png':
            d=diccionario['png']
            print(f'Su archivo es un MIME de tipo:\n {d}')
            
        elif tipo_minuscula=='pdf':
            e=diccionario['pdf']
            print(f'Su archivo es un MIME de tipo:\n {e}')
            
        elif tipo_minuscula=='txt':
            f=diccionario['txt']
            print(f'Su archivo es un MIME de tipo:\n {f}')
            
        elif tipo_minuscula=='zip':
            g=diccionario['zip']
            print(f'Su archivo es un MIME de tipo:\n {g}')
            
        else:
            print('application/octet-stream')
else:
 print('application/octet-stream')









'''
nombre, tipo=nombre_archivo.split('.')
tipo_minuscula=tipo.lower()

diccionario = {'jpg': 'image/jpeg' , 'gif' : 'image/gif', 'jpeg':'image/jpeg', 'png':'image/png', 'pdf': 'application/pdf', 'txt':'text/plain', 'zip':'application/zip'}

if tipo_minuscula in diccionario:
   if tipo_minuscula=='gif':
      
      a=diccionario['gif']
      print(f'Su archivo es un MIME de tipo:\n {a}')

   elif tipo_minuscula=='jpg':
      b=diccionario['jpg']
      print(f'Su archivo es un MIME de tipo:\n {b}')

   elif tipo_minuscula=='jpge':
      c=diccionario['jpge']
      print(f'Su archivo es un MIME de tipo:\n {c}')
          
   elif tipo_minuscula=='png':
      d=diccionario['png']
      print(f'Su archivo es un MIME de tipo:\n {d}')
      
   elif tipo_minuscula=='pdf':
      e=diccionario['pdf']
      print(f'Su archivo es un MIME de tipo:\n {e}')
      
   elif tipo_minuscula=='txt':
      f=diccionario['txt']
      print(f'Su archivo es un MIME de tipo:\n {f}')
      
   elif tipo_minuscula=='zip':
      g=diccionario['zip']
      print(f'Su archivo es un MIME de tipo:\n {g}')
      
else:
   print('application/octet-stream')

'''