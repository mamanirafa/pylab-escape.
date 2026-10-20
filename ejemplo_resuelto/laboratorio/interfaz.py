# ==============================================================
#  laboratorio/interfaz.py
#  Todo lo que tiene que ver con la PANTALLA: colores, títulos,
#  validación de datos. Separarlo en un módulo deja el resto
#  del código limpio y reutilizable.
# ==============================================================

import os
import sys

if "idlelib" in sys.modules:          # IDLE no muestra colores ANSI
    _COLOR = False
else:
    _COLOR = True
    os.system("")                     # habilita colores en Windows


def _c(codigo):
    return codigo if _COLOR else ""


TURQUESA = _c("\033[96m")
VERDE = _c("\033[92m")
AMARILLO = _c("\033[93m")
ROJO = _c("\033[91m")
AZUL = _c("\033[94m")
NEGRITA = _c("\033[1m")
FIN = _c("\033[0m")

COLOR_ESTADO = {"OK": VERDE, "POCOS": AMARILLO, "AGOTADO": ROJO}


def banner():
    print(f"""{TURQUESA}
  ╔════════════════════════════════════════════════╗
  ║   PyLab · Laboratorio de Robótica              ║
  ║   Sistema de préstamos de componentes          ║
  ╚════════════════════════════════════════════════╝{FIN}""")


def titulo(texto):
    print(f"\n{AZUL}{NEGRITA}  ── {texto} ──{FIN}")


def ok(texto):
    print(f"{VERDE}  ✔ {texto}{FIN}")


def error(texto):
    print(f"{ROJO}  ✖ {texto}{FIN}")


def aviso(texto):
    print(f"{AMARILLO}  ⚠ {texto}{FIN}")


def pedir_entero(mensaje, minimo, maximo):
    while True:
        dato = input(f"  {mensaje}").strip()
        if dato.isdigit() and minimo <= int(dato) <= maximo:
            return int(dato)
        error(f"Ingresá un número entre {minimo} y {maximo}.")


def pedir_texto(mensaje):
    while True:
        dato = input(f"  {mensaje}").strip()
        if dato != "":
            return dato
        error("No puede quedar vacío.")


def mostrar_componente(componente):
    color = COLOR_ESTADO[componente.estado()]
    print(f"  {componente.ficha()}  {color}{componente.estado()}{FIN}")


def barra(valor, total, largo=20):
    if total == 0:
        return ""
    llenos = round(valor / total * largo)
    return f"{TURQUESA}{'█' * llenos}{FIN}{'░' * (largo - llenos)}"
