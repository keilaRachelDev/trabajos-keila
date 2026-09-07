# INF 222 — Estructura de Datos · Semestre 2026-2

**Universidad de Panamá — Facultad de Informática, Electrónica y Comunicación**  
**Licenciatura en Desarrollo de Aplicaciones Tecnológicas**  
**Docente:** Angel R. Avila G. · angel.avila@up.ac.pa

---

## Bienvenida

**¿Primera vez aquí? Lee [`GUIA-ESTUDIANTE.md`](GUIA-ESTUDIANTE.md) primero** — es el checklist de qué hacer, en orden, desde antes de la primera clase hasta la sustentación final.

Este repositorio es la **plantilla** del curso (pública, para que puedas leer todo el contenido libremente). En la semana 1 obtienes tu propia copia de trabajo — el docente te la crea, o la creas tú mismo con "Use this template" — y ahí trabajas todo el semestre: laboratorios, avances del proyecto final y notas de clase. Detalle en `GUIA-ESTUDIANTE.md` y, para el docente, en `docente/GUIA-ENTREGAS-GITHUB.md`.

> **Regla de oro**: ninguna entrega se acepta por correo electrónico. Todo va en tu copia de este repositorio, organizado en la carpeta correcta, antes de la fecha límite.

---

## Estructura del repositorio

```
INF222-Estructura-de-Datos-2026-2/       (plantilla — 1 copia por estudiante, ver "Configuración inicial")
├── syllabus/               → Syllabus oficial del curso (créditos, evaluación, bibliografía)
├── politicas/              → Reglas del aula, política de IA, integridad académica
├── recursos/               → Guía de instalación de herramientas y referencias bibliográficas
├── docker/                 → Entorno reproducible opcional (Python 3.12 + pytest)
├── docente/                → Material de planificación del docente (syllabus fuente, plan de 15 semanas,
│                              rúbricas, guion de clase semana a semana, guía de entregas por GitHub)
├── .github/workflows/      → Autocalificación (corre pytest en cada push)
├── modulo-1-estructuras-lineales/
│   ├── semana-01/          → Intro + Big-O + Pilas
│   ├── semana-02/          → Pilas avanzadas + Colas
│   └── semana-03/          → Variantes de colas + Taller + Kickoff proyecto
├── modulo-2-estructuras-dinamicas/
│   ├── semana-04/          → Punteros y referencias
│   ├── semana-05/          → Listas enlazadas simples
│   ├── semana-06/          → Listas circulares
│   └── semana-07/          → Listas doblemente enlazadas + PARCIAL 1
├── modulo-3-recursividad-ordenacion-busqueda/
│   ├── semana-08/          → Recursividad
│   ├── semana-09/          → Ordenación (burbuja, selección, inserción)
│   ├── semana-10/          → Búsqueda + Checkpoint 1 proyecto
│   └── semana-11/          → Taller integrador + PARCIAL 2
├── modulo-4-arboles-grafos/
│   ├── semana-12/          → Árboles generales y binarios
│   ├── semana-13/          → BST (inserción, búsqueda, eliminación)
│   ├── semana-14/          → Grafos + BFS + DFS + Checkpoint 2 proyecto
│   └── semana-15/          → PARCIAL 3 + Sustentación final
└── examenes/               → Guías de estudio para los 3 parciales
```

> **El proyecto final vive en un repositorio aparte:** [`INF222-Proyecto-Final-2026-2`](../INF222-Proyecto-Final-2026-2/) — trabajo individual (este repo, una copia por estudiante) y trabajo en equipo (el proyecto, una copia por equipo de 3-4) se mantienen separados a propósito. El equipo crea su copia del repo de proyecto en la semana 3, tras el kickoff. Ver `docente/GUIA-ENTREGAS-GITHUB.md` para el paso a paso.

---

## Calendario de hitos y evaluaciones

| Semana | Fecha aprox. | Evento principal | Rubro |
|--------|-------------|-----------------|-------|
| 1  | ago 2026 | Lab 1: Pila con lista | Laboratorios |
| 2  | ago 2026 | Lab 2: Pila enlazada + Cola | Laboratorios |
| 3  | ago 2026 | Quiz formativo + Taller + **Kickoff proyecto** | Lab / Proyecto |
| 4  | ago 2026 | Lab 3: Referencias y aliasing | Laboratorios |
| 5  | sep 2026 | Lab 4: Lista enlazada simple | Laboratorios |
| 6  | sep 2026 | Lab 5: Listas circulares | Laboratorios |
| **7**  | sep 2026 | Lab 6: Lista doblemente enlazada · **PARCIAL 1** · **Propuesta formal** | Parciales / Proyecto |
| 8  | sep 2026 | Lab 7: Recursividad con IA declarada | Laboratorios |
| 9  | oct 2026 | Lab 8: Algoritmos de ordenación | Laboratorios |
| **10** | oct 2026 | Lab 9: Búsqueda · **Checkpoint 1 proyecto** | Lab / Proyecto |
| **11** | oct 2026 | Taller integrador · **PARCIAL 2** | Parciales |
| 12 | oct 2026 | Lab 10: Árbol binario y recorridos | Laboratorios |
| 13 | nov 2026 | Lab 11: BST | Laboratorios |
| **14** | nov 2026 | Lab 12: Grafos · **Checkpoint 2 proyecto** | Lab / Proyecto |
| **15** | nov 2026 | **PARCIAL 3** · **Sustentación final** · Coevaluación | Parciales / Proyecto |

---

## Sistema de evaluación

| Rubro | Porcentaje |
|-------|-----------|
| Exámenes Parciales (3 parciales, 10% c/u) | 30% |
| Prácticas / Laboratorios | 30% |
| Proyecto Final | 40% |
| **Total** | **100%** |

**Nota mínima de aprobación: 71%**

---

## Reglas para usar este repositorio

1. **Un commit por sesión de trabajo como mínimo.** No subas todo en el último minuto.
2. **Mensajes de commit descriptivos.** "semana-05: agrego método invertir() a ListaEnlazada" es correcto. "fix" o "asdf" no son aceptados.
3. **Todo va en la carpeta de la semana correspondiente.** No subas archivos en la raíz del repositorio.
4. **Declara el uso de IA en el archivo que entregues.** Lee la política completa en `politicas/politica-ia.md`.
5. **No compartas tu repositorio** con compañeros ni subas el código de otros. Integridad académica: lee `politicas/reglas-del-aula.md`.

---

## Horario de clases

| Sesión | Días | Hora |
|--------|------|------|
| Teoría (grupos A y B) | Martes | 8:45 p.m. – 10:30 p.m. |
| Teoría (grupos A y B) | Miércoles | 6:00 p.m. – 6:50 p.m. |
| Laboratorio Grupo A | Miércoles | 6:55 p.m. – 9:35 p.m. |
| Laboratorio Grupo B | Viernes | 7:50 p.m. – 10:30 p.m. |

---

## Configuración inicial (hazlo la primera semana)

Sigue los pasos en [`recursos/herramientas-setup.md`](recursos/herramientas-setup.md) para instalar Python 3, VS Code y configurar Git con tu cuenta de GitHub.

```bash
# Verifica tu instalación
python --version     # debe mostrar Python 3.x.x
git --version        # debe mostrar git version 2.x.x
```

Este repositorio (`INF222-Estructura-de-Datos-2026-2`) es la **plantilla del docente** — es público,
así que puedes leer todo su contenido libremente, pero tu trabajo va en **tu propia copia**, no aquí.
Dos formas de obtenerla (ver `GUIA-ESTUDIANTE.md`): el docente te la crea después de que respondas tu
usuario de GitHub en Google Classroom (te llega invitación por correo, acéptala), o la creas tú mismo
con el botón **"Use this template"** de esta página y agregas al docente como colaborador. En
cualquiera de los dos casos, clona tu copia (nunca esta plantilla):

```bash
git clone https://github.com/<tu-usuario>/<nombre-de-tu-repo>.git
cd <nombre-de-tu-repo>
```

**¿Prefieres no instalar Python localmente?** El repo incluye un entorno Docker opcional en `docker/` — ver [`docker/README.md`](docker/README.md). No es obligatorio, pero es el mismo entorno que corre la autocalificación automática en cada push (`.github/workflows/autograding.yml`), así que evita sorpresas de "en mi máquina sí funciona".

---

## Contacto

- **Correo:** angel.avila@up.ac.pa
- **Horario de atención:** (ver aula virtual)
- **Plataforma oficial:** Aula virtual institucional de la FIEC-UP
# trabajos-keila
