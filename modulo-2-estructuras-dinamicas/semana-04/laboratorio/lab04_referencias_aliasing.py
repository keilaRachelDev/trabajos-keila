"""
Lab 4 — Referencias y Aliasing en Python
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Keila Hurtado
Grupo: Salón 108
Fecha: 31 de octubre de 2026

Instrucciones:
    Para cada fragmento de código, PRIMERO escribe tu predicción en el comentario
    "PREDICCIÓN:", LUEGO ejecuta y registra el resultado real en "RESULTADO:".
    Usa Python Tutor para visualizar el estado de la memoria.
"""

import copy

print("=" * 55)
print("PARTE 1 — id() y referencias básicas")
print("=" * 55)

# Experimento 1.1: referencias a enteros
a = 42
b = a
# PREDICCIÓN: ¿son a y b el mismo objeto? (id(a) == id(b) → True/False)
# Mi predicción: True
print(f"1.1 id(a) == id(b): {id(a) == id(b)}")
# RESULTADO: True (acerté)
# EXPLICACIÓN: b = a no crea un objeto nuevo, solo hace que b apunte al mismo
#   objeto entero 42 que a. Por eso ambas variables tienen el mismo id().

# Experimento 1.2: reasignación no afecta al original
a = 42
b = a
b = 99
# PREDICCIÓN: ¿qué valor tiene a después de b = 99?
# Mi predicción: a = 42
print(f"1.2 a = {a}  (b fue reasignado a 99)")
# RESULTADO: a = 42 (acerté)
# EXPLICACIÓN: b = 99 no modifica el objeto 42 (los enteros son inmutables);
#   solo hace que b apunte a otro objeto (99). a sigue apuntando a 42.

print("\n" + "=" * 55)
print("PARTE 2 — Aliasing con listas")
print("=" * 55)

# Experimento 2.1: aliasing
lista_a = [1, 2, 3]
lista_b = lista_a          # ← esto NO copia la lista
lista_b.append(99)
# PREDICCIÓN: ¿qué contiene lista_a?
# Mi predicción: lista_a = [1, 2, 3, 99]
print(f"2.1 lista_a = {lista_a}  (lista_b.append(99))")
# RESULTADO: lista_a = [1, 2, 3, 99] (acerté)
# EXPLICACIÓN: lista_a y lista_b son dos nombres para el MISMO objeto lista
#   (aliasing). append() muta ese objeto, así que el cambio se ve por ambos.

# Experimento 2.2: copia superficial (shallow copy)
lista_a = [1, 2, 3]
lista_c = lista_a.copy()   # ← esto SÍ crea una copia nueva
lista_c.append(99)
# PREDICCIÓN: ¿qué contiene lista_a ahora?
# Mi predicción: lista_a = [1, 2, 3]
print(f"2.2 lista_a = {lista_a}  (lista_c.copy() y lista_c.append(99))")
# RESULTADO: lista_a = [1, 2, 3] (acerté)
# EXPLICACIÓN: copy() crea un objeto lista nuevo e independiente, por lo que
#   modificar lista_c no afecta a lista_a.

# Experimento 2.3: copia superficial con listas anidadas
original = [[1, 2], [3, 4]]
copia_superficial = original.copy()
copia_superficial[0].append(99)   # modifica la sublista
# PREDICCIÓN: ¿qué contiene original[0]?
# Mi predicción: original[0] = [1, 2, 99]
print(f"2.3 original[0] = {original[0]}  (shallow copy + append interno)")
# RESULTADO: original[0] = [1, 2, 99] (acerté)
# EXPLICACIÓN (por qué la shallow copy no fue suficiente aquí): la copia
#   superficial crea una lista externa nueva, pero sus elementos siguen siendo
#   las MISMAS sublistas del original. Al hacer append sobre la sublista, se
#   modifica un objeto compartido por ambas listas.

# Experimento 2.4: copia profunda (deep copy)
original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(original)
copia_profunda[0].append(99)
# PREDICCIÓN: ¿qué contiene original[0] ahora?
# Mi predicción: original[0] = [1, 2]
print(f"2.4 original[0] = {original[0]}  (deep copy + append interno)")
# RESULTADO: original[0] = [1, 2] (acerté)
# EXPLICACIÓN: deepcopy() copia recursivamente también las sublistas, así que
#   la copia no comparte ningún objeto mutable con el original.

print("\n" + "=" * 55)
print("PARTE 3 — Funciones: mutar vs. retornar copia")
print("=" * 55)


def agregar_elemento_in_situ(lista, elemento):
    """Modifica la lista original (mutación in situ)."""
    lista.append(elemento)
    # No retorna nada (retorna None implícitamente)

def agregar_elemento_copia(lista, elemento):
    """
    Retorna una nueva lista con el elemento agregado.
    La lista original NO se modifica.
    """
    nueva = lista.copy()   # copia superficial: objeto lista nuevo
    nueva.append(elemento)
    return nueva


# Prueba de mutar in situ
mi_lista = [1, 2, 3]
agregar_elemento_in_situ(mi_lista, 4)
print(f"3.1 in_situ:  mi_lista = {mi_lista}  (esperado: [1, 2, 3, 4])")

# Prueba de retornar copia
mi_lista = [1, 2, 3]
nueva_lista = agregar_elemento_copia(mi_lista, 4)
print(f"3.2 copia:    mi_lista  = {mi_lista}   (esperado: [1, 2, 3] — sin cambios)")
print(f"             nueva_lista = {nueva_lista}  (esperado: [1, 2, 3, 4])")

print("\n" + "=" * 55)
print("PARTE 4 — Predicciones adicionales (escribe ANTES de ejecutar)")
print("=" * 55)

# Fragmento 4.1
x = [10, 20, 30]
y = x
x = [40, 50]  # reasignación (no mutación)
# PREDICCIÓN: ¿qué contiene y?
# Mi predicción: y = [10, 20, 30]
print(f"4.1 y = {y}")
# RESULTADO: y = [10, 20, 30] (acerté)
# EXPLICACIÓN: x = [40, 50] no muta la lista original, solo hace que x apunte
#   a una lista nueva. y sigue apuntando a la lista [10, 20, 30].


# Fragmento 4.2
def modificar(lst):
    lst += [99]   # ¿es esto lo mismo que lst.append(99)?


nums = [1, 2, 3]
modificar(nums)
# PREDICCIÓN: ¿qué contiene nums?
# Mi predicción: nums = [1, 2, 3, 99]
print(f"4.2 nums = {nums}")
# RESULTADO: nums = [1, 2, 3, 99] (acerté)
# EXPLICACIÓN: en listas, += llama a __iadd__, que modifica la lista en su
#   lugar (como extend). Como lst y nums son el mismo objeto, el cambio se ve
#   afuera de la función.

# NOTA: += en listas llama a __iadd__ que modifica in situ,
#       mientras que + crea una lista nueva. Investiga la diferencia.
#   Diferencia: lst = lst + [99] crearía una lista nueva y reasignaría solo el
#   nombre local lst, por lo que nums NO cambiaría. En cambio lst += [99]
#   muta el objeto original, por lo que nums SÍ cambia.


# =============================================================================
# DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL
# =============================================================================
# Declaro que utilicé la herramienta de inteligencia artificial Claude
# (Anthropic) como apoyo para completar este laboratorio: implementación de
# la función agregar_elemento_copia y redacción de predicciones, resultados y
# explicaciones. Verifiqué el comportamiento ejecutando el código y con
# Python Tutor.
#
# Estudiante: Keila Hurtado
# Fecha: 31 de octubre de 2026