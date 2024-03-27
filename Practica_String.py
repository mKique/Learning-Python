# Mensaje de bienvenida
# Practica de leccion #2
# Miercoles 27 de marzo 2024
#-----------------------------------------------
# https://www.youtube.com/@coreyms
#------------------------------------------------

print ('HOLA!')

message = 'Hola Mundo'
print (message)

# Metodo para imprimir el caracter '
message = 'Hola\' Mundo'
print(message)

#Metodo para conocer la longitud del string
print(len(message))

#Metodo para desplegar pare del string
print(message[0:5])
print(message[6:])

#Metodo para cambiar los caracteres de minuscula a mayuscula y vicerversa
print(message.lower())
print(message.upper())

#Busquedas en el string
#Contar las coincidencias
print(message.count('Hello')) #devuelve el numero de veces que incidice el parametro en el string
print(message.find('World'))  #devuelve la posicion en donde se da la coincidencia de la busqueda. Si no lo encuentra, devuelve un -1

#Reemplazar un substring en el string
new_message = message.replace('World', 'Universe')
print(new_message) #tambien pudo ser message = message.replace('World','Universe')

#Concanetacion
#Usando el comando +
gretting = 'Hello'
name = 'Kique'
message = getting + ', ' + name 
print(message)

#Usando la instruccion format
message = '{},{}. Welcome!'.format(gretting,name)
print (message)

#Usando fString
message = f'{gretting}.{name}. Welcome!'
print(message)

#Para conocer los métodos disponibles
print(dir(name))

print(help(str))

print(help(str.lower))

