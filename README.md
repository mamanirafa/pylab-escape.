# 🤖 PyLab Escape · Laboratorio de Python

Sala de escape gamificada para aprender Python en el nivel secundario.
Un corte de luz trabó la puerta del **Laboratorio de Robótica** y la única forma de salir es reprogramar a **PyBot**, el robot del pañol. Cada sala enseña un concepto y entrega un dígito del código de la puerta.

| Sala | Escenario | Concepto |
|---|---|---|
| 1 | La terminal de encendido | Variables y tipos de datos |
| 2 | El sensor de la puerta | Estructuras condicionales |
| 3 | El estante de componentes | Listas y diccionarios |
| 4 | La cinta transportadora | Bucles `for` y `while` |
| 5 | El panel de control | Funciones |
| 6 | La fábrica de componentes | Clases y objetos |
| 7 | El árbol de familia | Herencia y sobreescritura |
| 8 | La caja de herramientas | Módulos, paquetes y librerías |

Cada sala tiene tres pasos: **📖 lectura** (con ejemplos ejecutables), **🧪 práctica guiada** (predecir, completar y ordenar código) y **🔐 desafío** (programar en Python real y pasar pruebas automáticas).
Al final, la **🏁 misión final** propone que cada equipo construya su propio sistema con clases, herencia y módulos.

## Funciones principales

- Python real en el navegador gracias a [Pyodide](https://pyodide.org) (no hay que instalar nada).
- Mensajes de error traducidos y explicados en castellano.
- Protección contra bucles infinitos.
- XP, pistas con costo, insignias, cronómetro y certificado imprimible.
- Panel docente: progreso por sala, informe para copiar, soluciones y desbloqueo para demostraciones.
- Lecturas previas imprimibles (`#lecturas`) para trabajar con aula invertida.
- Plantillas descargables (`main.py`, `modelos.py`, `funciones.py`) para la producción final.
- El progreso se guarda en el navegador de cada equipo.

## Publicarlo en GitHub Pages

1. Crear un repositorio nuevo (por ejemplo `pylab-escape`).
2. Subir **todo** el contenido de esta carpeta (`index.html`, `README.md`, `ejemplo_resuelto/`, `docs/`).
3. Ir a **Settings → Pages**, elegir la rama `main` y la carpeta `/ (root)`, y guardar.
4. En un par de minutos queda online en `https://<usuario>.github.io/pylab-escape/`.

> Necesita conexión a internet la primera vez para cargar Python (unos 10 MB). Si no hay conexión, la página funciona igual y verifica la estructura del código en modo simplificado.

## Estructura del repositorio

```
pylab-escape/
├── index.html                 ← la sala de escape (un solo archivo)
├── README.md
├── GUIA_EVALUACION.md         ← cómo revisar y probar cada entregable
├── docs/
│   ├── Secuencia_didactica_PyLab_Escape.docx
│   └── Secuencia_didactica_PyLab_Escape.pdf
└── ejemplo_resuelto/          ← programa del docente
    ├── main.py
    └── laboratorio/
        ├── __init__.py
        ├── componentes.py     ← clases y herencia
        ├── inventario.py      ← colecciones, bucles y funciones
        └── interfaz.py        ← pantalla y validaciones
```

Para correr el ejemplo: `cd ejemplo_resuelto` y después `python main.py`.

## Para quien evalúa

Ver **[GUIA_EVALUACION.md](GUIA_EVALUACION.md)**: dónde está cada punto de la consigna y un recorrido de prueba de 15 minutos. El código de la puerta es `47295183`.

## Adaptar el contenido

Todo el contenido (historias, lecturas, ejercicios, pruebas, pistas y temas de la misión final) está en el bloque **CONTENIDO DE LAS SALAS** al comienzo del `<script>` de `index.html`. Se puede cambiar sin tocar el motor del juego.

---
Secuencia didáctica para el curso *Programación avanzada con Python* (INET 2026) · Prof. Rafael Mamani · Ushuaia, Tierra del Fuego.
