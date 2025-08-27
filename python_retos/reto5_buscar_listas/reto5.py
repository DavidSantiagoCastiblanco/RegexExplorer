# Reto 5: Buscar listas de números en un texto usando regex
# Paso a paso:
# 1. Leer el texto de entrada.
# 2. Definir una expresión regular para encontrar listas de números (ej: [1, 2, 3]).
# 3. Buscar todas las listas en el texto.
# 4. Imprimir los resultados.

import re

texto = "Hoy en clase nos dividieron en grupos, el mío estaba formado por [3, 5, 7], mientras que el de mi amigo tenía a [2, 4, 6, 8]. Al final, todos terminamos trabajando juntos y el profesor nos calificó con [9, 10]."

# Expresión regular para listas de números
patron = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"

# Buscar todas las listas
listas = re.findall(patron, texto)

print("Listas encontradas:", listas)
# Paso a paso:
# 1. Cambia el texto de prueba.
# 2. Modifica la expresión regular si es necesario.
# 3. Ejecuta el script y observa los resultados.
