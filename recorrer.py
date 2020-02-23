lista = ['casa', 'auto', 'pelo', 'broche', 'juguete', 'mate']

while lista != []:
    # Armo la lista de las dos palabras a usar
    dos_palabras = lista[:2]
    # Saco de la lista original a las palabras que estoy recorriendo, para no volverlas a usar
    lista[:2] = []
    
    # Concateno las palabras
    frase = f'{dos_palabras[0]} y {dos_palabras[1]}'
    # imprimo el resultado
    print(frase)
