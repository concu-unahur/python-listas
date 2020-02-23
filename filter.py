lista = ['casa', 'auto', 'pelo', 'broche', 'juguete', 'mate']

class ManipuladorString:
  def empieza_con_a(self, string):
    return string[0] == 'a'

def es_corta(palabra):
  return len(palabra) < 5

# En Python, la función `filter` no devuelve una lista, por eso es que luego armamos la lista con `list`
filter_con_funcion = list(filter(es_corta, lista))
print(filter_con_funcion)

# También funciona pasándole un método de un objeto, porque en Python los métodos son funciones
manipulador = ManipuladorString()
filter_con_metodo = list(filter(manipulador.empieza_con_a, lista))
print(filter_con_metodo)

# La sintaxis `lambda x: ...` es equivalente a lo que en Wollok era `x => ...`
filter_con_lambda = list(filter(lambda palabra: len(palabra) > 5, lista))
print(filter_con_lambda)

# Otra magia de Python: las listas por comprensión (o list comprehension)
filter_list_comprehension = [ palabra for palabra in lista if palabra[0] == 'p' or palabra[0] == 'a' ]
print(filter_list_comprehension)

