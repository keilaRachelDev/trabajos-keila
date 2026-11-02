"""
Lab 11 — Taller Integrador: Ordenación + Búsqueda + Recursión
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Keila Hurtado
Grupo: Salon 108
Fecha: noviembre 2026

Este taller integra los tres grandes temas del Módulo 3. Deberás:
  - Elegir el algoritmo de ordenación más adecuado según el contexto.
  - Aplicar búsqueda binaria sobre la colección ordenada.
  - Diseñar una solución recursiva para un sub-problema.
  - Justificar las complejidades en las celdas marcadas como [ANÁLISIS].
"""

import sys
import time
import random
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(5000)  # potencia_lenta(2, 1000) necesita ~1000 llamadas anidadas


# =============================================================================
# PARTE 1: AGENDA DE CONTACTOS (ordenación + búsqueda)
# =============================================================================
# Un sistema simple de agenda ordena contactos por apellido y permite
# buscarlos por nombre completo de manera eficiente.

CONTACTOS_EJEMPLO = [
    {"nombre": "Carlos", "apellido": "Zúñiga",   "telefono": "6001-0001"},
    {"nombre": "María",  "apellido": "Alvarado",  "telefono": "6001-0002"},
    {"nombre": "Luis",   "apellido": "Morales",   "telefono": "6001-0003"},
    {"nombre": "Ana",    "apellido": "Batista",   "telefono": "6001-0004"},
    {"nombre": "Pedro",  "apellido": "Rodríguez", "telefono": "6001-0005"},
    {"nombre": "Sandra", "apellido": "López",     "telefono": "6001-0006"},
    {"nombre": "Jorge",  "apellido": "Chávez",    "telefono": "6001-0007"},
    {"nombre": "Elena",  "apellido": "Morales",   "telefono": "6001-0008"},  # mismo apellido que Luis
]


def _clave(contacto):
    """Clave de ordenación: primero apellido, luego nombre."""
    return (contacto["apellido"], contacto["nombre"])


def ordenar_contactos(contactos):
    """
    Ordena `contactos` (lista de dict) por 'apellido' y, en caso de empate,
    por 'nombre'. Debe retornar UNA NUEVA lista ordenada.
    [ANÁLISIS] Elegí merge sort: es O(n log n) en todos los casos, mientras
    que burbuja, selección e inserción son O(n²) y se vuelven lentos con
    agendas grandes. Además es estable y no modifica la lista original.
    Complejidad esperada: O(n log n) tiempo, O(n) espacio extra.
    """
    if len(contactos) <= 1:
        return list(contactos)
    medio = len(contactos) // 2
    izquierda = ordenar_contactos(contactos[:medio])
    derecha = ordenar_contactos(contactos[medio:])

    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if _clave(izquierda[i]) <= _clave(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def buscar_por_apellido(contactos_ordenados, apellido_buscado):
    """
    Busca TODOS los contactos cuyo 'apellido' == apellido_buscado.
    `contactos_ordenados` ya está ordenado por apellido.
    Retorna lista de contactos encontrados (puede ser más de uno).

    Estrategia:
      1. Búsqueda binaria para encontrar CUALQUIER coincidencia.
      2. Expandir hacia la izquierda y la derecha para capturar todas.
    Complejidad: O(log n + k) donde k = número de coincidencias.
    """
    izquierda = 0
    derecha = len(contactos_ordenados) - 1
    pos = -1
    while izquierda <= derecha:
        mid = (izquierda + derecha) // 2
        apellido = contactos_ordenados[mid]["apellido"]
        if apellido == apellido_buscado:
            pos = mid
            break
        elif apellido < apellido_buscado:
            izquierda = mid + 1
        else:
            derecha = mid - 1

    if pos == -1:
        return []

    inicio = pos
    while inicio > 0 and contactos_ordenados[inicio - 1]["apellido"] == apellido_buscado:
        inicio -= 1
    fin = pos
    while fin < len(contactos_ordenados) - 1 and contactos_ordenados[fin + 1]["apellido"] == apellido_buscado:
        fin += 1
    return contactos_ordenados[inicio:fin + 1]

def buscar_por_apellido(contactos_ordenados, apellido_buscado):
    """
    Busca TODOS los contactos cuyo 'apellido' == apellido_buscado.
    `contactos_ordenados` ya está ordenado por apellido.
    Retorna lista de contactos encontrados (puede ser más de uno).

    Estrategia sugerida:
      1. Usa búsqueda binaria para encontrar CUALQUIER coincidencia.
      2. Luego expande hacia la izquierda y la derecha para capturar todas.
    Complejidad esperada: O(log n + k) donde k = número de coincidencias.
    """
    # TODO
    pass


# =============================================================================
# PARTE 2: ESTADÍSTICAS RECURSIVAS
# =============================================================================

def suma_recursiva(nums):
    """
    Calcula la suma de `nums` usando recursión (sin usar sum()).
    Caso base: lista vacía → 0
    Complejidad: O(n).
    """
    if not nums:
        return 0
    return nums[0] + suma_recursiva(nums[1:])


def maximo_recursivo(nums):
    """
    Encuentra el máximo de `nums` usando recursión (sin usar max()).
    Caso base: lista de un elemento → ese elemento.
    Complejidad: O(n).
    """
    if len(nums) == 1:
        return nums[0]
    maximo_resto = maximo_recursivo(nums[1:])
    return nums[0] if nums[0] > maximo_resto else maximo_resto


def cuenta_mayores_recursivo(nums, umbral, i=0, acumulado=0):
    """
    Cuenta cuántos elementos de nums[i:] son estrictamente mayores que umbral.
    Usa recursión de cola (el resultado se va acumulando en `acumulado`).
    Complejidad: O(n).
    """
    if i >= len(nums):
        return acumulado
    if nums[i] > umbral:
        acumulado += 1
    return cuenta_mayores_recursivo(nums, umbral, i + 1, acumulado)

# =============================================================================
# PARTE 3: POTENCIAS Y EXPONENCIACIÓN RÁPIDA
# =============================================================================

def potencia_lenta(base, exp):
    """
    Calcula base^exp multiplicando una a una (O(n)).
    Ya implementada — úsala como referencia.
    """
    if exp == 0:
        return 1
    return base * potencia_lenta(base, exp - 1)


def potencia_rapida(base, exp):
    """
    Calcula base^exp con exponenciación por cuadrado.
    Observación clave: base^exp = (base^(exp//2))^2  si exp es par
                                  base * base^(exp-1) si exp es impar
    Complejidad: O(log n) — reduce el exponente a la mitad en cada paso.
    """
    if exp == 0:
        return 1
    if exp % 2 == 0:
        mitad = potencia_rapida(base, exp // 2)  # se calcula UNA sola vez
        return mitad * mitad
    return base * potencia_rapida(base, exp - 1)


# =============================================================================
# PARTE 4: PROBLEMA INTEGRADOR — TOP-K PRODUCTOS
# =============================================================================
# Dado un catálogo de productos con precios, encontrar los K más baratos
# de forma eficiente.

CATALOGO = [
    {"nombre": "Audífonos BT",     "precio": 45.99},
    {"nombre": "Cargador USB-C",   "precio": 12.50},
    {"nombre": "Funda celular",    "precio": 8.99},
    {"nombre": "Teclado inalám.",  "precio": 35.00},
    {"nombre": "Mouse ergonómico", "precio": 28.75},
    {"nombre": "Webcam HD",        "precio": 55.00},
    {"nombre": "Hub USB 4 puertos","precio": 18.00},
    {"nombre": "Soporte laptop",   "precio": 22.50},
    {"nombre": "Cable HDMI 2m",    "precio": 9.99},
    {"nombre": "Parlante portátil","precio": 39.00},
]


def top_k_baratos(catalogo, k):
    """
    Retorna los k productos más baratos del catálogo, ordenados de menor
    a mayor precio.
    Complejidad: O(n log n + k).
    """
    ordenado = sorted(catalogo, key=lambda p: p["precio"])
    return ordenado[:k]


def rango_precio(catalogo_ordenado, precio_min, precio_max):
    """
    Usando el catálogo YA ORDENADO por precio, retorna todos los
    productos cuyo precio está en [precio_min, precio_max].
    Usa búsqueda binaria (bisect) para encontrar los extremos del rango.
    Complejidad: O(log n + k) para la búsqueda (extraer la lista de precios
    cuesta O(n)).
    """
    precios = [p["precio"] for p in catalogo_ordenado]
    inicio = bisect_left(precios, precio_min)   # primer precio >= precio_min
    fin = bisect_right(precios, precio_max)     # primer precio > precio_max
    return catalogo_ordenado[inicio:fin]

# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":

    # ---- PARTE 1 ----
    print("=" * 60)
    print("PARTE 1: Agenda de Contactos")
    print("=" * 60)

    ordenados = ordenar_contactos(CONTACTOS_EJEMPLO)
    if ordenados:
        print("Contactos ordenados:")
        for c in ordenados:
            print(f"  {c['apellido']:15} {c['nombre']:10} {c['telefono']}")

        encontrados = buscar_por_apellido(ordenados, "Morales")
        print(f"\nBúsqueda 'Morales': {len(encontrados) if encontrados else 0} resultado(s)")
        for c in (encontrados or []):
            print(f"  {c['nombre']} {c['apellido']} — {c['telefono']}")

        no_encontrado = buscar_por_apellido(ordenados, "García")
        print(f"Búsqueda 'García': {no_encontrado}")  # esperado: [] o None

    # ---- PARTE 2 ----
    print("\n" + "=" * 60)
    print("PARTE 2: Estadísticas Recursivas")
    print("=" * 60)
    nums = [4, 7, 2, 9, 1, 5]
    print(f"Lista: {nums}")
    print(f"  suma_recursiva:           {suma_recursiva(nums)}  (esperado: 28)")
    print(f"  maximo_recursivo:         {maximo_recursivo(nums)}  (esperado: 9)")
    print(f"  cuenta_mayores(umbral=4): {cuenta_mayores_recursivo(nums, 4)}  (esperado: 3)")
    print(f"  suma_recursiva([]):       {suma_recursiva([])}  (esperado: 0)")

    # ---- PARTE 3 ----
    print("\n" + "=" * 60)
    print("PARTE 3: Potencias")
    print("=" * 60)
    pares_prueba = [(2, 10), (3, 5), (5, 0), (7, 3)]
    for base, exp in pares_prueba:
        lenta = potencia_lenta(base, exp)
        rapida = potencia_rapida(base, exp)
        estado = "OK" if lenta == rapida else "ERROR"
        print(f"  [{estado}] {base}^{exp} = {lenta} (rápida={rapida})")

    print("\nComparación de tiempos (base=2, exp=1000):")
    t0 = time.perf_counter()
    for _ in range(10_000):
        potencia_lenta(2, 1000)
    t_lenta = time.perf_counter() - t0

    t0 = time.perf_counter()
    for _ in range(10_000):
        potencia_rapida(2, 1000)
    t_rapida = time.perf_counter() - t0

    print(f"  Lenta O(n):        {t_lenta:.4f}s")
    print(f"  Rápida O(log n):   {t_rapida:.4f}s")

    # ---- PARTE 4 ----
    print("\n" + "=" * 60)
    print("PARTE 4: Top-K Productos")
    print("=" * 60)
    baratos = top_k_baratos(CATALOGO, 3)
    print("Top-3 más baratos:")
    for p in (baratos or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    cat_ord = sorted(CATALOGO, key=lambda p: p['precio'])
    rango = rango_precio(cat_ord, 10.0, 30.0)
    print("\nProductos entre $10 y $30:")
    for p in (rango or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    # ---- REFLEXIÓN ----
    print("\n" + "=" * 60)
    print("REFLEXIÓN FINAL")
    print("=" * 60)
    print("""
[ANÁLISIS] Responde en el docstring o en un comentario:

1. ¿Qué algoritmo de ordenación elegiste en la Parte 1 y por qué
   es apropiado para ordenar una lista de dicts por apellido?

2. ¿Cuántas comparaciones haría la búsqueda binaria en una agenda
   de 1 000 contactos en el peor caso?

3. ¿Cuántas llamadas recursivas hace potencia_rapida(2, 64)?
   Dibuja el árbol de llamadas.
""")
# =============================================================================
# [ANÁLISIS] RESPUESTAS
# 1. Elegí merge sort. Es O(n log n) siempre, estable, y compara las claves
#    (apellido, nombre) sin importar que sean dicts. Los algoritmos O(n²)
#    de burbuja, selección e inserción escalan mal con agendas grandes.
#
# 2. En una agenda de 1,000 contactos, la búsqueda binaria hace como máximo
#    10 comparaciones en el peor caso, porque 2^10 = 1,024 >= 1,000
#    (log2(1000) ≈ 10). La secuencial haría hasta 1,000.
#
# 3. potencia_rapida(2, 64) hace 8 llamadas en total (la inicial y 7
#    recursivas). El exponente baja 64 → 32 → 16 → 8 → 4 → 2 → 1 → 0,
#    así que el árbol es una cadena sin ramas, a diferencia de fibonacci:
#
#    potencia_rapida(2, 64)
#      └─ potencia_rapida(2, 32)
#           └─ potencia_rapida(2, 16)
#                └─ potencia_rapida(2, 8)
#                     └─ potencia_rapida(2, 4)
#                          └─ potencia_rapida(2, 2)
#                               └─ potencia_rapida(2, 1)   (impar: 2 * ...)
#                                    └─ potencia_rapida(2, 0) → 1
# =============================================================================

# =============================================================================
# DECLARACIÓN DE USO DE IA
# Usé Claude (Anthropic) para implementar las funciones y comprender los temas de este lab.
# y para redacte las respuestas del análisis y ejecuté las pruebas.
# =============================================================================
"""
Lab 11 — Taller Integrador: Ordenación + Búsqueda + Recursión
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Keila Hurtado
Grupo: Salon 108
Fecha: noviembre 2026

Este taller integra los tres grandes temas del Módulo 3. Deberás:
  - Elegir el algoritmo de ordenación más adecuado según el contexto.
  - Aplicar búsqueda binaria sobre la colección ordenada.
  - Diseñar una solución recursiva para un sub-problema.
  - Justificar las complejidades en las celdas marcadas como [ANÁLISIS].
"""

import sys
import time
import random
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(5000)  # potencia_lenta(2, 1000) necesita ~1000 llamadas anidadas


# =============================================================================
# PARTE 1: AGENDA DE CONTACTOS (ordenación + búsqueda)
# =============================================================================
# Un sistema simple de agenda ordena contactos por apellido y permite
# buscarlos por nombre completo de manera eficiente.

CONTACTOS_EJEMPLO = [
    {"nombre": "Carlos", "apellido": "Zúñiga",   "telefono": "6001-0001"},
    {"nombre": "María",  "apellido": "Alvarado",  "telefono": "6001-0002"},
    {"nombre": "Luis",   "apellido": "Morales",   "telefono": "6001-0003"},
    {"nombre": "Ana",    "apellido": "Batista",   "telefono": "6001-0004"},
    {"nombre": "Pedro",  "apellido": "Rodríguez", "telefono": "6001-0005"},
    {"nombre": "Sandra", "apellido": "López",     "telefono": "6001-0006"},
    {"nombre": "Jorge",  "apellido": "Chávez",    "telefono": "6001-0007"},
    {"nombre": "Elena",  "apellido": "Morales",   "telefono": "6001-0008"},  # mismo apellido que Luis
]


def _clave(contacto):
    """Clave de ordenación: primero apellido, luego nombre."""
    return (contacto["apellido"], contacto["nombre"])


def ordenar_contactos(contactos):
    """
    Ordena `contactos` (lista de dict) por 'apellido' y, en caso de empate,
    por 'nombre'. Debe retornar UNA NUEVA lista ordenada.
    [ANÁLISIS] Elegí merge sort: es O(n log n) en todos los casos, mientras
    que burbuja, selección e inserción son O(n²) y se vuelven lentos con
    agendas grandes. Además es estable y no modifica la lista original.
    Complejidad esperada: O(n log n) tiempo, O(n) espacio extra.
    """
    if len(contactos) <= 1:
        return list(contactos)
    medio = len(contactos) // 2
    izquierda = ordenar_contactos(contactos[:medio])
    derecha = ordenar_contactos(contactos[medio:])

    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if _clave(izquierda[i]) <= _clave(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def buscar_por_apellido(contactos_ordenados, apellido_buscado):
    """
    Busca TODOS los contactos cuyo 'apellido' == apellido_buscado.
    `contactos_ordenados` ya está ordenado por apellido.
    Retorna lista de contactos encontrados (puede ser más de uno).

    Estrategia:
      1. Búsqueda binaria para encontrar CUALQUIER coincidencia.
      2. Expandir hacia la izquierda y la derecha para capturar todas.
    Complejidad: O(log n + k) donde k = número de coincidencias.
    """
    izquierda = 0
    derecha = len(contactos_ordenados) - 1
    pos = -1
    while izquierda <= derecha:
        mid = (izquierda + derecha) // 2
        apellido = contactos_ordenados[mid]["apellido"]
        if apellido == apellido_buscado:
            pos = mid
            break
        elif apellido < apellido_buscado:
            izquierda = mid + 1
        else:
            derecha = mid - 1

    if pos == -1:
        return []

    inicio = pos
    while inicio > 0 and contactos_ordenados[inicio - 1]["apellido"] == apellido_buscado:
        inicio -= 1
    fin = pos
    while fin < len(contactos_ordenados) - 1 and contactos_ordenados[fin + 1]["apellido"] == apellido_buscado:
        fin += 1
    return contactos_ordenados[inicio:fin + 1]

def buscar_por_apellido(contactos_ordenados, apellido_buscado):
    """
    Busca TODOS los contactos cuyo 'apellido' == apellido_buscado.
    `contactos_ordenados` ya está ordenado por apellido.
    Retorna lista de contactos encontrados (puede ser más de uno).

    Estrategia sugerida:
      1. Usa búsqueda binaria para encontrar CUALQUIER coincidencia.
      2. Luego expande hacia la izquierda y la derecha para capturar todas.
    Complejidad esperada: O(log n + k) donde k = número de coincidencias.
    """
    # TODO
    pass


# =============================================================================
# PARTE 2: ESTADÍSTICAS RECURSIVAS
# =============================================================================

def suma_recursiva(nums):
    """
    Calcula la suma de `nums` usando recursión (sin usar sum()).
    Caso base: lista vacía → 0
    Complejidad: O(n).
    """
    if not nums:
        return 0
    return nums[0] + suma_recursiva(nums[1:])


def maximo_recursivo(nums):
    """
    Encuentra el máximo de `nums` usando recursión (sin usar max()).
    Caso base: lista de un elemento → ese elemento.
    Complejidad: O(n).
    """
    if len(nums) == 1:
        return nums[0]
    maximo_resto = maximo_recursivo(nums[1:])
    return nums[0] if nums[0] > maximo_resto else maximo_resto


def cuenta_mayores_recursivo(nums, umbral, i=0, acumulado=0):
    """
    Cuenta cuántos elementos de nums[i:] son estrictamente mayores que umbral.
    Usa recursión de cola (el resultado se va acumulando en `acumulado`).
    Complejidad: O(n).
    """
    if i >= len(nums):
        return acumulado
    if nums[i] > umbral:
        acumulado += 1
    return cuenta_mayores_recursivo(nums, umbral, i + 1, acumulado)

# =============================================================================
# PARTE 3: POTENCIAS Y EXPONENCIACIÓN RÁPIDA
# =============================================================================

def potencia_lenta(base, exp):
    """
    Calcula base^exp multiplicando una a una (O(n)).
    Ya implementada — úsala como referencia.
    """
    if exp == 0:
        return 1
    return base * potencia_lenta(base, exp - 1)


def potencia_rapida(base, exp):
    """
    Calcula base^exp con exponenciación por cuadrado.
    Observación clave: base^exp = (base^(exp//2))^2  si exp es par
                                  base * base^(exp-1) si exp es impar
    Complejidad: O(log n) — reduce el exponente a la mitad en cada paso.
    """
    if exp == 0:
        return 1
    if exp % 2 == 0:
        mitad = potencia_rapida(base, exp // 2)  # se calcula UNA sola vez
        return mitad * mitad
    return base * potencia_rapida(base, exp - 1)


# =============================================================================
# PARTE 4: PROBLEMA INTEGRADOR — TOP-K PRODUCTOS
# =============================================================================
# Dado un catálogo de productos con precios, encontrar los K más baratos
# de forma eficiente.

CATALOGO = [
    {"nombre": "Audífonos BT",     "precio": 45.99},
    {"nombre": "Cargador USB-C",   "precio": 12.50},
    {"nombre": "Funda celular",    "precio": 8.99},
    {"nombre": "Teclado inalám.",  "precio": 35.00},
    {"nombre": "Mouse ergonómico", "precio": 28.75},
    {"nombre": "Webcam HD",        "precio": 55.00},
    {"nombre": "Hub USB 4 puertos","precio": 18.00},
    {"nombre": "Soporte laptop",   "precio": 22.50},
    {"nombre": "Cable HDMI 2m",    "precio": 9.99},
    {"nombre": "Parlante portátil","precio": 39.00},
]


def top_k_baratos(catalogo, k):
    """
    Retorna los k productos más baratos del catálogo, ordenados de menor
    a mayor precio.
    Complejidad: O(n log n + k).
    """
    ordenado = sorted(catalogo, key=lambda p: p["precio"])
    return ordenado[:k]


def rango_precio(catalogo_ordenado, precio_min, precio_max):
    """
    Usando el catálogo YA ORDENADO por precio, retorna todos los
    productos cuyo precio está en [precio_min, precio_max].
    Usa búsqueda binaria (bisect) para encontrar los extremos del rango.
    Complejidad: O(log n + k) para la búsqueda (extraer la lista de precios
    cuesta O(n)).
    """
    precios = [p["precio"] for p in catalogo_ordenado]
    inicio = bisect_left(precios, precio_min)   # primer precio >= precio_min
    fin = bisect_right(precios, precio_max)     # primer precio > precio_max
    return catalogo_ordenado[inicio:fin]

# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":

    # ---- PARTE 1 ----
    print("=" * 60)
    print("PARTE 1: Agenda de Contactos")
    print("=" * 60)

    ordenados = ordenar_contactos(CONTACTOS_EJEMPLO)
    if ordenados:
        print("Contactos ordenados:")
        for c in ordenados:
            print(f"  {c['apellido']:15} {c['nombre']:10} {c['telefono']}")

        encontrados = buscar_por_apellido(ordenados, "Morales")
        print(f"\nBúsqueda 'Morales': {len(encontrados) if encontrados else 0} resultado(s)")
        for c in (encontrados or []):
            print(f"  {c['nombre']} {c['apellido']} — {c['telefono']}")

        no_encontrado = buscar_por_apellido(ordenados, "García")
        print(f"Búsqueda 'García': {no_encontrado}")  # esperado: [] o None

    # ---- PARTE 2 ----
    print("\n" + "=" * 60)
    print("PARTE 2: Estadísticas Recursivas")
    print("=" * 60)
    nums = [4, 7, 2, 9, 1, 5]
    print(f"Lista: {nums}")
    print(f"  suma_recursiva:           {suma_recursiva(nums)}  (esperado: 28)")
    print(f"  maximo_recursivo:         {maximo_recursivo(nums)}  (esperado: 9)")
    print(f"  cuenta_mayores(umbral=4): {cuenta_mayores_recursivo(nums, 4)}  (esperado: 3)")
    print(f"  suma_recursiva([]):       {suma_recursiva([])}  (esperado: 0)")

    # ---- PARTE 3 ----
    print("\n" + "=" * 60)
    print("PARTE 3: Potencias")
    print("=" * 60)
    pares_prueba = [(2, 10), (3, 5), (5, 0), (7, 3)]
    for base, exp in pares_prueba:
        lenta = potencia_lenta(base, exp)
        rapida = potencia_rapida(base, exp)
        estado = "OK" if lenta == rapida else "ERROR"
        print(f"  [{estado}] {base}^{exp} = {lenta} (rápida={rapida})")

    print("\nComparación de tiempos (base=2, exp=1000):")
    t0 = time.perf_counter()
    for _ in range(10_000):
        potencia_lenta(2, 1000)
    t_lenta = time.perf_counter() - t0

    t0 = time.perf_counter()
    for _ in range(10_000):
        potencia_rapida(2, 1000)
    t_rapida = time.perf_counter() - t0

    print(f"  Lenta O(n):        {t_lenta:.4f}s")
    print(f"  Rápida O(log n):   {t_rapida:.4f}s")

    # ---- PARTE 4 ----
    print("\n" + "=" * 60)
    print("PARTE 4: Top-K Productos")
    print("=" * 60)
    baratos = top_k_baratos(CATALOGO, 3)
    print("Top-3 más baratos:")
    for p in (baratos or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    cat_ord = sorted(CATALOGO, key=lambda p: p['precio'])
    rango = rango_precio(cat_ord, 10.0, 30.0)
    print("\nProductos entre $10 y $30:")
    for p in (rango or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    # ---- REFLEXIÓN ----
    print("\n" + "=" * 60)
    print("REFLEXIÓN FINAL")
    print("=" * 60)
    print("""
[ANÁLISIS] Responde en el docstring o en un comentario:

1. ¿Qué algoritmo de ordenación elegiste en la Parte 1 y por qué
   es apropiado para ordenar una lista de dicts por apellido?

2. ¿Cuántas comparaciones haría la búsqueda binaria en una agenda
   de 1 000 contactos en el peor caso?

3. ¿Cuántas llamadas recursivas hace potencia_rapida(2, 64)?
   Dibuja el árbol de llamadas.
""")
# =============================================================================
# [ANÁLISIS] RESPUESTAS
# 1. Elegí merge sort. Es O(n log n) siempre, estable, y compara las claves
#    (apellido, nombre) sin importar que sean dicts. Los algoritmos O(n²)
#    de burbuja, selección e inserción escalan mal con agendas grandes.
#
# 2. En una agenda de 1,000 contactos, la búsqueda binaria hace como máximo
#    10 comparaciones en el peor caso, porque 2^10 = 1,024 >= 1,000
#    (log2(1000) ≈ 10). La secuencial haría hasta 1,000.
#
# 3. potencia_rapida(2, 64) hace 8 llamadas en total (la inicial y 7
#    recursivas). El exponente baja 64 → 32 → 16 → 8 → 4 → 2 → 1 → 0,
#    así que el árbol es una cadena sin ramas, a diferencia de fibonacci:
#
#    potencia_rapida(2, 64)
#      └─ potencia_rapida(2, 32)
#           └─ potencia_rapida(2, 16)
#                └─ potencia_rapida(2, 8)
#                     └─ potencia_rapida(2, 4)
#                          └─ potencia_rapida(2, 2)
#                               └─ potencia_rapida(2, 1)   (impar: 2 * ...)
#                                    └─ potencia_rapida(2, 0) → 1
# =============================================================================

# =============================================================================
# DECLARACIÓN DE USO DE IA
# Usé Claude (Anthropic) para implementar las funciones y comprender los temas de este lab.
# y redacte las respuestas del análisis y ejecuté las pruebas.
# =============================================================================
