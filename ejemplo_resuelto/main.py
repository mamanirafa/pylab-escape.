# ==============================================================
#   PyLab · Sistema de préstamos del Laboratorio de Robótica
#   Ejemplo resuelto por el docente - Secuencia "PyLab Escape"
#   Programación avanzada con Python - INET 2026
#   Autor: Rafael Mamani
# --------------------------------------------------------------
#   Cómo ejecutarlo: abrir esta carpeta y correr  python main.py
#   Estructura:
#     main.py                     ← programa principal (este archivo)
#     laboratorio/                ← PAQUETE
#        componentes.py           ← CLASES + HERENCIA
#        inventario.py            ← colecciones, bucles, funciones
#        interfaz.py              ← pantalla y validaciones
# ==============================================================

# ---- MÓDULOS: traemos lo que necesitamos de cada archivo ----
from laboratorio.inventario import (cargar_inventario, buscar,
                                    filtrar_por_tipo, registrar_prestamo,
                                    registrar_devolucion, resumen)
from laboratorio import interfaz as ui


def ver_inventario(inventario):
    ui.titulo("INVENTARIO")
    print("  [1] Todos  [2] Sensores  [3] Actuadores  [4] Placas")
    opcion = ui.pedir_entero("Filtro: ", 1, 4)
    tipos = {1: "Todos", 2: "Sensor", 3: "Actuador", 4: "Placa"}
    lista = filtrar_por_tipo(inventario, tipos[opcion])
    for componente in lista:
        ui.mostrar_componente(componente)


def prestar(inventario, prestamos):
    ui.titulo("NUEVO PRÉSTAMO")
    estudiante = ui.pedir_texto("Estudiante: ").title()
    codigo = ui.pedir_texto("Código del componente (ej. S01): ")
    componente = buscar(inventario, codigo)
    if componente is None:
        ui.error(f"No existe el código {codigo}.")
        return
    ui.mostrar_componente(componente)
    unidades = ui.pedir_entero("¿Cuántas unidades? ", 1, 20)
    exito, mensaje = registrar_prestamo(inventario, prestamos,
                                        estudiante, codigo, unidades)
    if exito:
        ui.ok(mensaje)
        if componente.estado() != "OK":
            ui.aviso(f"{componente.nombre}: quedan {componente.disponibles()} libres.")
    else:
        ui.error(mensaje)


def devolver(prestamos):
    ui.titulo("DEVOLUCIÓN")
    if len(prestamos) == 0:
        ui.aviso("No hay préstamos activos.")
        return
    estudiante = ui.pedir_texto("¿Quién devuelve? ")
    cantidad = registrar_devolucion(prestamos, estudiante)
    if cantidad > 0:
        ui.ok(f"Devolución registrada: {cantidad} ítem(s) de {estudiante.title()}.")
    else:
        ui.error(f"{estudiante.title()} no tiene préstamos activos.")


def ver_prestamos(prestamos):
    ui.titulo("PRÉSTAMOS ACTIVOS")
    if len(prestamos) == 0:
        ui.ok("Todo está en el laboratorio.")
    for numero, prestamo in enumerate(prestamos, start=1):
        print(f"  {numero}. {prestamo}")


def ver_resumen(inventario):
    ui.titulo("TABLERO DEL LABORATORIO")
    for tipo, (total, prestados) in resumen(inventario).items():
        print(f"  {tipo:<9} {ui.barra(prestados, total)} {prestados}/{total} afuera")


# ==============================================================
#   PROGRAMA PRINCIPAL
# ==============================================================
def main():
    inventario = cargar_inventario()     # lista de objetos
    prestamos = []                       # lista de objetos Prestamo

    ui.banner()
    encargado = ui.pedir_texto("👩‍🔧 ¿Quién está a cargo del pañol hoy? ").title()
    print(f"  Hola, {encargado}. Hay {len(inventario)} tipos de componentes cargados. 🤖")

    opciones = {
        1: "Ver inventario",
        2: "Prestar componente",
        3: "Registrar devolución",
        4: "Ver préstamos activos",
        5: "Tablero del laboratorio",
        0: "Cerrar el pañol",
    }

    opcion = -1
    while opcion != 0:
        print(f"\n  {ui.NEGRITA}MENÚ{ui.FIN}")
        for numero, texto in opciones.items():
            print(f"  {ui.TURQUESA}[{numero}]{ui.FIN} {texto}")
        opcion = ui.pedir_entero("Opción: ", 0, 5)

        if opcion == 1:
            ver_inventario(inventario)
        elif opcion == 2:
            prestar(inventario, prestamos)
        elif opcion == 3:
            devolver(prestamos)
        elif opcion == 4:
            ver_prestamos(prestamos)
        elif opcion == 5:
            ver_resumen(inventario)

    if len(prestamos) > 0:
        ui.aviso(f"Préstamos sin devolver: {len(prestamos)}. ¡Anotalos!")
    print(f"\n  {ui.TURQUESA}Pañol cerrado. ¡Buen trabajo, {encargado}! 🔒{ui.FIN}\n")


# Solo se ejecuta si corremos ESTE archivo (no si lo importan)
if __name__ == "__main__":
    main()
