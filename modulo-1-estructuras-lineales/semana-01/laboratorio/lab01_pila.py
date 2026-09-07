"""
Lab 1 — Implementación de la clase Pila (Stack)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Keila Hurtado
Grupo: 108
Fecha: 7 de septiembre 2026
"""


class Pila:
    """
    Implementación de una pila (stack) usando una lista de Python como
    contenedor interno. Principio LIFO: el último elemento insertado es
    el primero en salir.
    """

    def __init__(self):
        """Inicializa una pila vacía."""
        self._datos = []  # el tope de la pila está en el índice -1

    def push(self, dato):
        """
        Agrega `dato` al tope de la pila.
        Complejidad: O(1) amortizado.
        """
        # TODO: implementa este método
        self._datos.append(dato)

    def pop(self):
        """
        Elimina y retorna el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        Complejidad: O(1) amortizado.
        """
        # TODO: implementa este método
        # Recuerda verificar si la pila está vacía antes de operar
        if self.is_empty():
           raise IndexError("La pila está vacía")
        return self._datos.pop()

    def peek(self):
        """
        Retorna (sin eliminar) el elemento del tope de la pila.
        Lanza IndexError si la pila está vacía.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        if self.is_empty():
          raise IndexError("La pila está vacía")
        return self._datos[-1]

    def is_empty(self):
        """
        Retorna True si la pila no contiene elementos, False en caso contrario.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        return len(self._datos) == 0

    def size(self):
        """
        Retorna el número de elementos en la pila.
        Complejidad: O(1).
        """
        # TODO: implementa este método
        return len(self._datos)

    def __str__(self):
        """
        Retorna una representación legible de la pila.
        Formato sugerido: Pila (tope -> base): [3, 2, 1]
        Complejidad: O(n).
        """
        # TODO: implementa este método
        return f"Pila (tope -> base): {self._datos[::-1]}"


# =============================================================================
# CASOS DE PRUEBA
# Agrega aquí al menos 5 casos de prueba. Usa print() para mostrar resultados
# y verifica que cada caso produce la salida esperada.
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("Pruebas de la clase Pila")
    print("=" * 50)

    # Caso 1: Pila vacía
    pila = Pila()
    print("Caso 1 - Pila vacía:", pila.is_empty())

    # Caso 2: push de 3 elementos
    pila.push(1)
    pila.push(2)
    pila.push(3)
    print("Caso 2 - Tamaño:", pila.size())

    # Caso 3: peek sin modificar la pila
    print("Caso 3 - Tope:", pila.peek())
    print("Caso 3 - Tamaño después de peek:", pila.size())

    # Caso 4: pop retorna el tope
    print("Caso 4 - Elemento eliminado:", pila.pop())

    # Caso 5: pop en pila vacía lanza IndexError
    pila_vacia = Pila()

    try:
      pila_vacia.pop()
    except IndexError:
      print("Caso 5 - IndexError detectado correctamente")
      
