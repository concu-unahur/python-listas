lista = ['casa', 'auto', 'pelo', 'broche', 'juguete', 'mate']

class ManipuladorString:
  def reverse(self, string):
    return string[::-1]

def primera_letra(palabra):
  return palabra[0]

# En Python, la función `map` no devuelve una lista, por eso es que luego armamos la lista con `list`
map_con_funcion = list(map(primera_letra, lista))
print(map_con_funcion)

# También funciona pasándole un método de un objeto, porque en Python los métodos son funciones
manipulador = ManipuladorString()
map_con_metodo = list(map(manipulador.reverse, lista))
print(map_con_metodo)

# La sintaxis `lambda x: ...` es equivalente a lo que en Wollok era `x => ...`
map_con_lambda = list(map(lambda palabra: palabra.upper(), lista))
print(map_con_lambda)

# Otra magia de Python: las listas por comprensión (o list comprehension)
map_list_comprehension = [ len(palabra) for palabra in lista ]
print(map_list_comprehension)

