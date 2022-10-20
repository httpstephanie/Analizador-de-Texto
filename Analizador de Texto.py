#Crear programa que le pida al usuario ingresar un texto, ingrese 3 letras, que el codigo procese el texto y devuelva, cuantas veces aparece cada letra, cuantas palabras hay en total, primer y ultima letra
texto =input('Escribe una frase: ')
letras = []

texto = texto.lower() #todo enn minusculas
letras.append(input('Ingresa la primer letra: ').lower()) #Append es metodo para ingresar algo INDICE 0
letras.append(input('Ingresa la segunda letra: ').lower()) #INDICE 1
letras.append(input('Ingresa la tercer letra: ').lower())  #INDICE 2

print('\n')
print('Cantidad de letras')
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2]) #Va a contar cuantas veces hay un a letra en la lista "letras" 

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces")


print('\n')
print('Cantidad de palabras')
palabras =texto.split() #.split separa el texto en porciones
print(f'Hemos encontrado {len(palabras)} palabras en la frase')

print('\n')
print('Primer y ultima letra')
letra_inicio = texto [0]
letra_final = texto[-1]
print(f"La primer letra es {letra_inicio} y la ultima letra es {letra_final}")

print('\n')
print('Texto Invertido')
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f'Si invertimos el orden de tu frase se veria asi: {texto_invertido}')

print('\n')
print('Buscar la palabra Python')
buscar_python = 'python' in texto
dic = {True:"Si", False: "No"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en la frase")

