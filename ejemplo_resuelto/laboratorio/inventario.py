# ==============================================================
#  laboratorio/inventario.py
#  FUNCIONES que trabajan con la COLECCIÓN de componentes
#  y con los préstamos (listas, diccionarios, bucles).
# ==============================================================

from laboratorio.componentes import Sensor, Actuador, Placa


class Prestamo:
    """Registro de quién se llevó qué."""

    def __init__(self, estudiante, componente, unidades):
        self.estudiante = estudiante
        self.componente = componente      # guarda el OBJETO completo
        self.unidades = unidades

    def __str__(self):
        return (f"{self.estudiante:<14} → {self.unidades} x "
                f"{self.componente.nombre} [{self.componente.codigo}]")


def cargar_inventario():
    """Crea los objetos del laboratorio y los devuelve en una lista."""
    return [
        Sensor("S01", "Sensor ultrasónico HC-SR04", 8, "distancia"),
        Sensor("S02", "Sensor de temperatura LM35", 6, "temperatura"),
        Sensor("S03", "Fotorresistor LDR", 10, "luz"),
        Actuador("A01", "Servomotor SG90", 6, 5),
        Actuador("A02", "Motor DC con reductora", 4, 6),
        Actuador("A03", "Buzzer activo", 5, 5),
        Placa("P01", "Arduino UNO", 5, 14),
        Placa("P02", "ESP32 DevKit", 3, 25),
    ]


def buscar(inventario, codigo):
    """Recorre la lista y devuelve el componente con ese código (o None)."""
    for componente in inventario:
        if componente.codigo == codigo.upper():
            return componente
    return None


def filtrar_por_tipo(inventario, tipo):
    resultado = []
    for componente in inventario:
        if tipo == "Todos" or componente.tipo == tipo:
            resultado.append(componente)
    return resultado


def registrar_prestamo(inventario, prestamos, estudiante, codigo, unidades):
    """Intenta prestar. Devuelve un mensaje para mostrar al usuario."""
    componente = buscar(inventario, codigo)
    if componente is None:
        return False, f"No existe el código {codigo}."
    if componente.prestar(unidades):
        prestamos.append(Prestamo(estudiante, componente, unidades))
        return True, f"Prestado: {unidades} x {componente.nombre} a {estudiante}."
    if componente.tipo == "Placa" and unidades > 1:
        return False, "Las placas se prestan de a una."
    return False, f"No alcanza: quedan {componente.disponibles()} libres."


def registrar_devolucion(prestamos, estudiante):
    """Devuelve TODO lo que tenía un estudiante. Retorna cuántos ítems."""
    devueltos = 0
    for prestamo in prestamos[:]:            # copia: vamos a borrar
        if prestamo.estudiante.lower() == estudiante.lower():
            prestamo.componente.devolver(prestamo.unidades)
            prestamos.remove(prestamo)
            devueltos = devueltos + 1
    return devueltos


def resumen(inventario):
    """Diccionario con totales por tipo: {'Sensor': [total, prestados], ...}"""
    totales = {}
    for componente in inventario:
        if componente.tipo not in totales:
            totales[componente.tipo] = [0, 0]
        totales[componente.tipo][0] += componente.cantidad
        totales[componente.tipo][1] += componente.prestados
    return totales
