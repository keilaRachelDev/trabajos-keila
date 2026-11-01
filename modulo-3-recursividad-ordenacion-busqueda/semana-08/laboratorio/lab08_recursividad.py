"""
Lab 8 — Recursividad (con uso declarado de IA)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Keila Hurtado
Grupo: Salon 108
Fecha: noviembre 2026

=============================================================
DECLARACIÓN DE USO DE IA.
=============================================================
Herramienta usada      : Claude (Anthropic)
Para qué se usó        : implementar factorial, las tres versiones de
                         fibonacci y Torres de Hanoi; obtener el trazado
                         de fibonacci.
Qué hice yo            : integré el código, ejecuté las pruebas, reescribí
                         el trazado con mis palabras y dibujé el diagrama
Puedo explicar todo    : (No, con honestidad)
=============================================================
"""

import time
from functools import lru_cache

# =============================================================================
# PARTE 1 — FACTORIAL
# =============================================================================

def factorial(n):
    """
    Calcula n! de forma recursiva.
    Caso base: factorial(0) = 1
    Caso recursivo: factorial(n) = n × factorial(n-1)
    Complejidad: O(n) tiempo, O(n) espacio (por la pila de llamadas).
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


# =============================================================================
# PARTE 2 — FIBONACCI
# =============================================================================

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de Fibonacci recursivamente.
    ⚠️  Esta implementación es ineficiente: O(2^n) llamadas.
    Solo para propósitos de análisis y trazado.
    """
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


@lru_cache(maxsize=None)
def fibonacci_memoizado(n):
    """
    Calcula el n-ésimo número de Fibonacci con memoización.
    O(n) tiempo, O(n) espacio.
    """
    if n <= 1:
        return n
    return fibonacci_memoizado(n - 1) + fibonacci_memoizado(n - 2)


def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci iterativamente.
    O(n) tiempo, O(1) espacio.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# =============================================================================
# PARTE 3 — TORRES DE HANOI
# =============================================================================

movimientos = []  # lista global para registrar los movimientos

def torres_de_hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de Torres de Hanoi para n discos.
    Parámetros:
        n:         número de discos a mover
        origen:    poste donde están los n discos al inicio
        destino:   poste al que deben llegar todos los discos
        auxiliar:  poste auxiliar
    Efecto: agrega strings a `movimientos` con cada movimiento.
    Complejidad: O(2^n - 1) movimientos.
    """
    if n == 1:
        movimientos.append(f"Mover disco 1 de {origen} a {destino}")
        return
    # 1. Mover n-1 discos de origen a auxiliar (usando destino como aux)
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    # 2. Mover el disco más grande de origen a destino
    movimientos.append(f"Mover disco {n} de {origen} a {destino}")
    # 3. Mover n-1 discos de auxiliar a destino (usando origen como aux)
    torres_de_hanoi(n - 1, auxiliar, destino, origen)

# =============================================================================
# PARTE 4 — TRAZADO CON IA (obligatorio)
# =============================================================================
"""
INSTRUCCIONES:
1. Ejecuta fibonacci_recursivo(5) en tu mente o en papel primero.
2. Luego consulta un asistente de IA con este prompt:
   "Muéstrame el trazado paso a paso de la pila de llamadas de fibonacci(5)
    usando la versión recursiva simple (sin memoización). Usa indentación para
    mostrar la jerarquía de llamadas."
3. Copia el trazado que generó la IA en el espacio de abajo.
4. Reescríbelo CON TUS PROPIAS PALABRAS en el espacio "Trazado propio".
   Dibuja también el diagrama ASCII de la pila de llamadas.

TRAZADO GENERADO POR IA:
fib(5)
  fib(4)
    fib(3)
      fib(2)
        fib(1) → 1
        fib(0) → 0
      fib(2) = 1
      fib(1) → 1
    fib(3) = 2
    fib(2)
      fib(1) → 1
      fib(0) → 0
    fib(2) = 1
  fib(4) = 3
  fib(3)
    fib(2)
      fib(1) → 1
      fib(0) → 0
    fib(2) = 1
    fib(1) → 1
  fib(3) = 2
fib(5) = 3 + 2 = 5

Total: 15 llamadas. fib(3) se calcula 2 veces, fib(2) 3 veces.


TRAZADO PROPIO (reescrito por el estudiante, sin copiar de la IA):
Cuando llamo a fib(5), primero llama a fib(4), y fib(4) llama a fib(3),
y así hasta llegar a fib(1), que es un caso base y devuelve 1 sin llamar
a nadie más. Entonces se empieza a subir: fib(2) llama también a fib(0),
que devuelve 0, suma 1 + 0 = 1 y devuelve ese resultado a fib(3).
Cada llamada hace lo mismo: pide primero el resultado de n-1, luego el de
n-2, los suma y se lo devuelve a quien la llamó.

El problema es que se repiten cálculos: fib(3) se calcula 2 veces y
fib(2) se calcula 3 veces, porque cada llamada ignora lo que ya
calcularon las otras. Para fib(5) son 15 llamadas, y como cada llamada
genera otras dos, el número se casi duplica cada vez que n sube en 1.
Por eso es O(2^n) y fib(35) tarda segundos, mientras que la memoizada y
la iterativa lo hacen casi al instante.


DIAGRAMA ASCII DE LA PILA DE LLAMADAS (dibujado por ti):
[dibuja aquí la pila de llamadas paso a paso]
Momento 1: máxima profundidad    Momento 2: fib(1) retorna 1
| fib(1) | ← tope               | fib(2) | ← tope (ahora llama a fib(0))
| fib(2) |                      | fib(3) |
| fib(3) |                      | fib(4) |
| fib(4) |                      | fib(5) | ← base
| fib(5) | ← base

Momento 3: entra fib(0)          Momento 4: fib(0) retorna 0,
| fib(0) | ← tope               fib(2) retorna 1; fib(3) llama a fib(1)
| fib(2) |                      | fib(1) | ← tope
| fib(3) |                      | fib(3) |
| fib(4) |                      | fib(4) |
| fib(5) | ← base               | fib(5) | ← base

Momento 5: fib(1) retorna 1,     Momento 6: al final
fib(3) retorna 2;                | fib(5) | ← única llamada
fib(4) llama a fib(2)            fib(5) = 3 + 2 = 5, retorna y la
| fib(2) | ← tope               pila queda vacía
| fib(4) |
| fib(5) | ← base
"""


# =============================================================================
# CASOS DE PRUEBA Y COMPARACIÓN DE TIEMPOS
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 1 — Factorial")
    print("=" * 55)
    for n in [0, 1, 5, 10]:
        print(f"  factorial({n}) = {factorial(n)}")

    print("\n" + "=" * 55)
    print("PARTE 2 — Fibonacci: comparación de eficiencia")
    print("=" * 55)
    casos = [10, 20, 30, 35]
    for n in casos:
        t0 = time.perf_counter()
        r = fibonacci_recursivo(n)
        t_rec = time.perf_counter() - t0

        t0 = time.perf_counter()
        m = fibonacci_memoizado(n)
        t_mem = time.perf_counter() - t0

        t0 = time.perf_counter()
        i = fibonacci_iterativo(n)
        t_it = time.perf_counter() - t0

        assert r == m == i, f"Discrepancia en fib({n}): {r}, {m}, {i}"
        print(f"  fib({n:2d}) = {r:10d} | recursivo: {t_rec:.4f}s | memo: {t_mem:.6f}s | iter: {t_it:.6f}s")

    print("\n" + "=" * 55)
    print("PARTE 3 — Torres de Hanoi (n=3)")
    print("=" * 55)
    movimientos.clear()
    torres_de_hanoi(3, "A", "C", "B")
    print(f"  Total de movimientos para n=3: {len(movimientos)} (esperado: 7)")
    for mov in movimientos:
        print(f"  {mov}")

    print(f"\n  Para n=10: {2**10 - 1} movimientos (2^10 - 1)")
    print(f"  Para n=20: {2**20 - 1:,} movimientos — ¿ves por qué O(2^n) escala mal?")
