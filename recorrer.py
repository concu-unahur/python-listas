def primera_letra(palabra):
    return palabra[0]

def concatena_letras(lista):
    return ''.join(lista)

lista = ['casa', 'auto', 'pelo', 'broche', 'juguete', 'mate']

while lista != []:
    # armo la lista de las dos palabras a usar
    letras = map(primera_letra, lista[:2])
    letras_lista = list(letras)
    # concateno las primeras letras de cada palabra
    letras_concat = concatena_letras(letras_lista)
    # imprimo el resultado
    print(letras_concat)
    # saco de la lista a las palabras que acabo de concatenar, para no volverlas a usar
    lista[:2]=[]