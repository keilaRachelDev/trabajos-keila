"""
Lab 6 — Listas Circulares y Problema de Josephus
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Keila Hurtado
Grupo: _Salon 108
Fecha: octubre 2026
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# =============================================================================
# PARTE 1: LISTA ENLAZADA CIRCULAR
# El último nodo apunta al primero (no a None).
# =============================================================================

class ListaCircular:
    """
    Lista enlazada circular. El atributo `_cola` apunta al ÚLTIMO nodo
    (cuyo `siguiente` es el primer nodo). Esto permite insertar al
    inicio y al final en O(1).
    """

    def __init__(self):
        self._cola = None   # nodo del final; _cola.siguiente = primer nodo
        self._tamanio = 0

    def insertar_inicio(self, dato):
        """Inserta dato al inicio de la lista. O(1)."""
        nuevo = Nodo(dato)
        if self._cola is None:
            nuevo.siguiente = nuevo  # apunta a sí mismo (único nodo)
            self._cola = nuevo
        else:
            nuevo.siguiente = self._cola.siguiente  # nuevo → primero
            self._cola.siguiente = nuevo            # cola → nuevo (ahora nuevo es el primero)
        self._tamanio += 1

    def insertar_final(self, dato):
        """Inserta dato al final de la lista. O(1)."""
        self.insertar_inicio(dato)   # inserta al inicio...
        self._cola = self._cola.siguiente  # ...luego avanza la cola (el recién insertado es el último)

    def eliminar_inicio(self):
        """Elimina y retorna el dato del inicio. Lanza IndexError si está vacía."""
        if self._cola is None:
            raise IndexError("eliminar en lista circular vacía")
        primero = self._cola.siguiente
        if primero == self._cola:    # solo un nodo
            self._cola = None
        else:
            self._cola.siguiente = primero.siguiente
        self._tamanio -= 1
        return primero.dato

    def recorrer(self):
        """Retorna una lista con todos los datos en orden desde el inicio."""
        resultado = []
        if self._cola is None:
            return resultado
        actual = self._cola.siguiente  # primero
        for _ in range(self._tamanio):
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def es_vacia(self):
        return self._cola is None

    def tamanio(self):
        return self._tamanio

    def __str__(self):
        datos = self.recorrer()
        if not datos:
            return "Lista circular vacía"
        return " → ".join(str(d) for d in datos) + " → (inicio)"


# =============================================================================
# PARTE 2: LISTA CIRCULAR CON NODO CABEZA (SENTINELA)
# Hay un nodo fijo (centinela) que no contiene dato útil.
# La lista está vacía cuando cabeza.siguiente == cabeza.
# =============================================================================

class ListaCircularConCabeza:
    """
    Lista enlazada circular con nodo centinela.
    El centinela siempre existe (no puede eliminarse).
    La lista vacía: centinela.siguiente = centinela.
    """

    def __init__(self):
        self._centinela = Nodo(None)
        self._centinela.siguiente = self._centinela
        self._tamanio = 0

    def insertar_inicio(self, dato):
        """Inserta dato justo después del centinela (al inicio lógico). O(1)."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self._centinela.siguiente
        self._centinela.siguiente = nuevo
        self._tamanio += 1

    def insertar_final(self, dato):
        """Inserta dato justo antes del centinela (al final). O(n) sin puntero al final."""
        nuevo = Nodo(dato)
        ultimo = self._centinela
        # Recorre hasta el nodo cuyo siguiente es el centinela
        while ultimo.siguiente is not self._centinela:
            ultimo = ultimo.siguiente
        nuevo.siguiente = self._centinela
        ultimo.siguiente = nuevo
        self._tamanio += 1

    def eliminar(self, dato):
        """Elimina la primera ocurrencia de dato. Retorna True si se encontró."""
        anterior = self._centinela
        actual = self._centinela.siguiente
        while actual is not self._centinela:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente  # desencadena el nodo
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def recorrer(self):
        """Retorna lista con todos los datos desde el inicio hasta antes del centinela."""
        resultado = []
        actual = self._centinela.siguiente
        while actual is not self._centinela:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def es_vacia(self):
        return self._centinela.siguiente is self._centinela

    def __str__(self):
        datos = self.recorrer()
        if not datos:
            return "[C] → [C] (vacía)"
        return "[C] → " + " → ".join(str(d) for d in datos) + " → [C]"

# =============================================================================
# PARTE 3: PROBLEMA DE JOSEPHUS
# n personas en círculo, contar hasta k, eliminar, repetir.
# =============================================================================

def josephus(n, k):
    """
    Resuelve el problema de Josephus usando ListaCircular.
    n: número de personas (numeradas del 1 al n)
    k: cuenta hasta k para eliminar a alguien
    Retorna: el número de la persona que sobrevive.
    """
    lista = ListaCircular()
    for i in range(1, n + 1):
        lista.insertar_final(i)

    while lista.tamanio() > 1:
        # _cola es el nodo anterior al primero de la ronda;
        # avanzar k-1 veces lo deja justo antes de la víctima
        for _ in range(k - 1):
            lista._cola = lista._cola.siguiente
        victima = lista._cola.siguiente
        lista._cola.siguiente = victima.siguiente  # desenlaza a la víctima
        lista._tamanio -= 1

    return lista._cola.dato


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 1: Lista Circular")
    print("=" * 55)
    lc = ListaCircular()
    lc.insertar_final(1)
    lc.insertar_final(2)
    lc.insertar_final(3)
    lc.insertar_inicio(0)
    print(lc)           # 0 → 1 → 2 → 3 → (inicio)
    print(f"Tamaño: {lc.tamanio()}")
    dato = lc.eliminar_inicio()
    print(f"Eliminado del inicio: {dato}")
    print(lc)           # 1 → 2 → 3 → (inicio)

    print("\n" + "=" * 55)
    print("PARTE 2: Lista Circular con Nodo Cabeza")
    print("=" * 55)
    lcc = ListaCircularConCabeza()
    print(f"¿Vacía? {lcc.es_vacia()}")
    lcc.insertar_inicio(10)
    lcc.insertar_inicio(20)
    lcc.insertar_final(5)
    print(lcc)           # [C] → 20 → 10 → 5 → [C]
    lcc.eliminar(10)
    print(f"Después de eliminar 10: {lcc}")

    print("\n" + "=" * 55)
    print("PARTE 3: Problema de Josephus")
    print("=" * 55)
    print(f"josephus(7, 3) = {josephus(7, 3)}  (esperado: 4)")
    print(f"josephus(5, 2) = {josephus(5, 2)}  (esperado: 3)")
    print(f"josephus(1, 5) = {josephus(1, 5)}  (esperado: 1)")
    
    

# =============================================================================
# DIAGRAMA COMPARATIVO
# =============================================================================
#
# 1) LISTA SIMPLE
#    El último nodo apunta a None.
#
#    primero
#       ↓
#     [10] → [20] → [30] → None
#
#
# 2) LISTA CIRCULAR (con _cola)
#    El último nodo apunta de vuelta al primero.
#    Se guarda _cola (el último), y _cola.siguiente es el primero.
#
#                     _cola
#                       ↓
#     ┌→ [10] → [20] → [30] ─┐
#     │   (primero)          │
#     └──────────────────────┘
#
#    Lista con un solo nodo (apunta a sí mismo):
#
#       _cola
#         ↓
#        [10] ─┐
#         ↑────┘
#
#
# 3) LISTA CIRCULAR CON NODO CABEZA (centinela)
#    [C] siempre existe y no guarda dato útil.
#    El último nodo apunta a [C], no al primer nodo real.
#
#     ┌→ [C] → [10] → [20] → [30] ─┐
#     │                            │
#     └────────────────────────────┘
#
#    Lista vacía (el centinela apunta a sí mismo):
#
#        [C] ─┐
#         ↑───┘
#
#
# COMPARACIÓN
# -----------------------------------------------------------------------------
#                    Simple          Circular         Circular con cabeza
# Fin del recorrido  siguiente=None  contar nodos     volver a [C]
#                                    o volver al
#                                    primero
# Lista vacía        primero=None    _cola=None       [C].siguiente = [C]
# Insertar al final  O(n) sin cola   O(1) con _cola   O(n) sin puntero final
# Caso especial al   sí (lista       sí (lista        no, [C] siempre
# insertar/eliminar  vacía)          vacía)           existe
# =============================================================================
# =============================================================================
# EXPLICACIÓN
# - insertar_final: recorro hasta el último nodo (el que apunta al centinela)
#   y enlazo ahí el nuevo nodo, que apunta al centinela.
# - eliminar: recorro con anterior y actual; al encontrar el dato, anterior
#   salta al siguiente de actual. Si vuelvo al centinela, retorno False.
# - josephus: _cola es el nodo anterior al que empieza la cuenta. Avanzo
#   k-1 veces y desenlazo al siguiente. Repito hasta que quede un nodo.
#   Debo estar en el anterior porque, para borrar un nodo, hay que cambiar
#   el enlace del que lo apunta.
# - El centinela evita casos especiales: siempre hay un nodo antes del primero.
# =============================================================================

# =============================================================================
#declaracion de uso de inteligencia artificial.
# Declaro que utilize la herramienta de IA claude para ayudarme a completar este código.
# =============================================================================
