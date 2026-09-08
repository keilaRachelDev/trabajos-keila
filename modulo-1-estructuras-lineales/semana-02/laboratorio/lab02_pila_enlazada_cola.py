"""
Lab 2 — Pila Enlazada, Cola y Simulador de Impresión

INF 222 Estructura de Datos · Semestre 2026-2

Estudiante: keila hurtado
Grupo: 108
Fecha: 7 de septiembre 2026
"""


# =============================================================================
# PARTE 1: NODO (base para la pila enlazada y la cola)
# =============================================================================

class Nodo:
    """Nodo básico con un dato y una referencia al siguiente nodo."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# =============================================================================
# PARTE 2: PILA ENLAZADA
# =============================================================================

class PilaEnlazada:
    """
    Pila implementada con nodos enlazados.

    El tope de la pila es la cabeza de la lista de nodos.
    """

    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    def push(self, dato):
        """Inserta dato en el tope. Complejidad: O(1)."""

        nuevo = Nodo(dato)
        nuevo.siguiente = self._cabeza
        self._cabeza = nuevo
        self._tamanio += 1

    def pop(self):
        """Elimina y retorna el dato del tope. Lanza IndexError si está vacía."""

        if self.is_empty():
            raise IndexError("La pila está vacía")

        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1

        return dato

    def peek(self):
        """Retorna (sin eliminar) el dato del tope. Lanza IndexError si está vacía."""

        if self.is_empty():
            raise IndexError("La pila está vacía")

        return self._cabeza.dato

    def is_empty(self):
        """Retorna True si la pila está vacía."""

        return self._cabeza is None

    def size(self):
        """Retorna el número de elementos."""

        return self._tamanio

    def __str__(self):
        """Representación: tope → ... → base."""

        elementos = []
        actual = self._cabeza

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        return "Pila (tope -> base): [" + ", ".join(elementos) + "]"


# =============================================================================
# PARTE 3: VERIFICADOR DE PARÉNTESIS BALANCEADOS
# =============================================================================

def parentesis_balanceados(cadena):
    """
    Retorna True si todos los pares de paréntesis, corchetes y llaves
    en cadena están correctamente balanceados; False en caso contrario.

    Usa la clase PilaEnlazada.

    Ejemplos:
        parentesis_balanceados("({[]})")  → True
        parentesis_balanceados("([)]")    → False
        parentesis_balanceados("{[")      → False
    """

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    aperturas = set(pares.values())

    pila = PilaEnlazada()

    for caracter in cadena:

        if caracter in aperturas:
            pila.push(caracter)

        elif caracter in pares:

            if pila.is_empty():
                return False

            tope = pila.pop()

            if tope != pares[caracter]:
                return False

    return pila.is_empty()


# =============================================================================
# PARTE 4: COLA (QUEUE)
# =============================================================================

class Cola:
    """
    Cola implementada con nodos enlazados.

    - enqueue agrega al final (cola)
    - dequeue saca del frente (cabeza)
    """

    def __init__(self):
        self._frente = None
        self._final = None
        self._tamanio = 0

    def enqueue(self, dato):
        """Agrega dato al final de la cola. Complejidad: O(1)."""

        nuevo = Nodo(dato)

        if self.is_empty():
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo

        self._tamanio += 1

    def dequeue(self):
        """Elimina y retorna el dato del frente. Lanza IndexError si está vacía."""

        if self.is_empty():
            raise IndexError("La cola está vacía")

        dato = self._frente.dato
        self._frente = self._frente.siguiente
        self._tamanio -= 1

        if self._frente is None:
            self._final = None

        return dato

    def front(self):
        """Retorna (sin eliminar) el dato del frente. Lanza IndexError si está vacía."""

        if self.is_empty():
            raise IndexError("La cola está vacía")

        return self._frente.dato

    def is_empty(self):
        return self._frente is None

    def size(self):
        return self._tamanio

    def __str__(self):
        """Representación: frente → ... → final."""

        elementos = []
        actual = self._frente

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        return "Cola (frente -> final): [" + ", ".join(elementos) + "]"


# =============================================================================
# PARTE 5: SIMULADOR DE COLA DE IMPRESIÓN (mini-proyecto)
# =============================================================================

class TrabajoImpresion:
    """Representa un trabajo en la cola de impresión."""

    def __init__(self, nombre, paginas):
        self.nombre = nombre
        self.paginas = paginas

    def __str__(self):
        return f"'{self.nombre}' ({self.paginas} pág.)"


def simulador_impresion(trabajos):
    """
    Simula una cola de impresión.

    Recibe una lista de tuplas (nombre, páginas).

    Imprime en orden de llegada (FIFO) el nombre de cada trabajo
    y cuántas páginas tiene.

    Al final muestra el total de páginas impresas.
    """

    cola = Cola()
    total_paginas = 0

    # Encolar todos los trabajos
    for nombre, paginas in trabajos:
        trabajo = TrabajoImpresion(nombre, paginas)
        cola.enqueue(trabajo)

    # Procesar los trabajos en orden FIFO
    numero = 1

    while not cola.is_empty():
        trabajo = cola.dequeue()

        print(
            f"  Imprimiendo trabajo {numero}: "
            f"{trabajo.nombre} - {trabajo.paginas} páginas"
        )

        total_paginas += trabajo.paginas
        numero += 1

    print(f"  Total de páginas impresas: {total_paginas}")


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("PARTE 2: Pila Enlazada")
    print("=" * 55)

    pila = PilaEnlazada()

    print("Pila inicialmente vacía:", pila.is_empty())

    pila.push("A")
    pila.push("B")
    pila.push("C")

    print("Pila después de push:", pila)
    print("Tope:", pila.peek())
    print("Tamaño:", pila.size())

    elemento = pila.pop()

    print("Elemento eliminado:", elemento)
    print("Pila después de pop:", pila)
    print("Nuevo tope:", pila.peek())
    print("Tamaño:", pila.size())


    print("\n" + "=" * 55)
    print("PARTE 3: Verificador de Paréntesis Balanceados")
    print("=" * 55)

    casos = [
        ("({[]})", True),
        ("([)]", False),
        ("{[", False),
        ("", True),
        ("3 + (4 * [2])", True),
    ]

    for cadena, esperado in casos:
        resultado = parentesis_balanceados(cadena)
        estado = "OK" if resultado == esperado else "ERROR"

        print(
            f"  [{estado}] '{cadena}' → "
            f"{resultado} (esperado: {esperado})"
        )


    print("\n" + "=" * 55)
    print("PARTE 4: Cola")
    print("=" * 55)

    cola = Cola()

    print("Cola inicialmente vacía:", cola.is_empty())

    cola.enqueue("Primero")
    cola.enqueue("Segundo")
    cola.enqueue("Tercero")

    print("Cola después de enqueue:", cola)
    print("Frente:", cola.front())
    print("Tamaño:", cola.size())

    elemento = cola.dequeue()

    print("Elemento eliminado:", elemento)
    print("Cola después de dequeue:", cola)
    print("Nuevo frente:", cola.front())
    print("Tamaño:", cola.size())


    print("\n" + "=" * 55)
    print("PARTE 5: Simulador de Impresión")
    print("=" * 55)

    trabajos = [
        ("Tesis cap1", 12),
        ("Factura", 1),
        ("Informe anual", 8),
        ("CV", 2)
    ]

    simulador_impresion(trabajos)