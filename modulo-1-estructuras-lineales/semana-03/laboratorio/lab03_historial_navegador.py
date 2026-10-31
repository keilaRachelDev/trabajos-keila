"""
Lab 3 — Simulador de Historial de Navegador (Taller Integrador)
INF 222 Estructura de Datos · Semestre 2026-2
Estudiante: Keila Hurtado
Grupo: Salón 108
Fecha: 15 de septiembre de 2026

Descripción:
    Simula el comportamiento del historial de un navegador web usando DOS pilas:
    - pila_atras:    páginas a las que se puede volver
    - pila_adelante: páginas a las que se puede avanzar
    Se utiliza la clase Pila implementada en lab01.
"""

class Pila:
    """Pila implementada con lista de Python (copia de lab01)."""

    def __init__(self):
        self._datos = []

    def push(self, dato):
        self._datos.append(dato)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop en pila vacía")
        return self._datos.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek en pila vacía")
        return self._datos[-1]

    def is_empty(self):
        return len(self._datos) == 0

    def size(self):
        return len(self._datos)

    def __str__(self):
        return f"Pila (tope→base): {list(reversed(self._datos))}"


# =============================================================================
# SIMULADOR DE HISTORIAL
# =============================================================================

class HistorialNavegador:
    """
    Simula el historial de un navegador web con botones Atrás y Adelante.
    """

    def __init__(self, pagina_inicial="about:blank"):
        self._actual = pagina_inicial
        self._pila_atras = Pila()
        self._pila_adelante = Pila()

    def visitar(self, url):
        """
        Visita una nueva URL.
        - La página actual pasa a la pila de atrás.
        - La pila de adelante se vacía (ya no hay futuro después de un desvío).
        """
        self._pila_atras.push(self._actual)
        self._actual = url
        self._pila_adelante = Pila()

    def atras(self):
        """
        Navega a la página anterior (si existe).
        - La página actual pasa a la pila de adelante.
        - La nueva página actual es el tope de la pila de atrás.
        Retorna la URL a la que se navegó, o None si no hay página anterior.
        """
        if self._pila_atras.is_empty():
            return None

        self._pila_adelante.push(self._actual)
        self._actual = self._pila_atras.pop()

        return self._actual

    def adelante(self):
        """
        Navega a la siguiente página (si existe).
        - La página actual pasa a la pila de atrás.
        - La nueva página actual es el tope de la pila de adelante.
        Retorna la URL a la que se navegó, o None si no hay página siguiente.
        """
        if self._pila_adelante.is_empty():
            return None

        self._pila_atras.push(self._actual)
        self._actual = self._pila_adelante.pop()

        return self._actual

    def pagina_actual(self):
        """Retorna la URL de la página actualmente visible."""
        return self._actual

    def estado(self):
        """Imprime el estado completo del historial para depuración."""
        print(f"  Actual:   {self._actual}")
        print(f"  Atrás:    {self._pila_atras}")
        print(f"  Adelante: {self._pila_adelante}")


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Simulador de Historial de Navegador")
    print("=" * 55)

    nav = HistorialNavegador()

    print("\n--- Visitando páginas ---")
    nav.visitar("google.com")
    nav.visitar("wikipedia.org")
    nav.visitar("github.com")
    nav.visitar("up.ac.pa")
    print(f"Página actual: {nav.pagina_actual()}")
    nav.estado()
    assert nav.pagina_actual() == "up.ac.pa"

    print("\n--- Navegando Atrás x2 ---")
    print(f"  → {nav.atras()}")
    print(f"  → {nav.atras()}")
    print(f"Página actual: {nav.pagina_actual()}")
    nav.estado()
    assert nav.pagina_actual() == "wikipedia.org"

    print("\n--- Navegando Adelante x1 ---")
    print(f"  → {nav.adelante()}")
    print(f"Página actual: {nav.pagina_actual()}")
    nav.estado()
    assert nav.pagina_actual() == "github.com"

    print("\n--- Visitar nueva página (borra el adelante) ---")
    nav.visitar("classroom.github.com")
    print(f"Página actual: {nav.pagina_actual()}")
    nav.estado()
    assert nav.pagina_actual() == "classroom.github.com"

    print("\n--- Intentar adelante cuando no hay ---")
    resultado = nav.adelante()
    print(f"  → {resultado}  (esperado: None)")
    assert resultado is None

    print("\n--- Intentar atrás hasta el inicio ---")
    while nav.atras() is not None:
        pass

    print(f"Página actual: {nav.pagina_actual()}  (esperado: about:blank)")
    assert nav.pagina_actual() == "about:blank"
    resultado_extra = nav.atras()
    print(f"Otro atrás → {resultado_extra}  (esperado: None)")
    assert resultado_extra is None

    print("\n✔ Todas las pruebas pasaron correctamente.")


# =============================================================================
# DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL
# =============================================================================
# Declaro que utilicé herramientas de inteligencia artificial como apoyo en
# este trabajo:
#   - ChatGPT (OpenAI): me apoyé en esta herramienta para desarrollar parte
#     del código del simulador.
#   - Claude (Anthropic): lo usé para revisar el código, corregir detalles de
#     presentación (encabezado y comentarios de la plantilla) y agregar
#     aserciones (assert) a los casos de prueba.
# Revisé y trate de compreder el código y los cambios sugeridos antes de incluirlos
# en este trabajo.
