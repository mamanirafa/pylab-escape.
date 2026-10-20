# ==============================================================
#  laboratorio/componentes.py
#  CLASES y HERENCIA del sistema de préstamos del Laboratorio
#  de Robótica.
#
#  Componente  (clase padre)
#     ├── Sensor     (hija)
#     ├── Actuador   (hija)
#     └── Placa      (hija)
# ==============================================================


class Componente:
    """Cualquier pieza del laboratorio que se puede prestar."""

    tipo = "Componente"      # atributo de clase: lo comparten todos
    icono = "🔩"

    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo          # ej: "S01"
        self.nombre = nombre          # ej: "Sensor ultrasónico HC-SR04"
        self.cantidad = cantidad      # cuántos tiene el laboratorio
        self.prestados = 0            # cuántos están afuera

    # ---------- métodos comunes a TODOS los componentes ----------
    def disponibles(self):
        return self.cantidad - self.prestados

    def prestar(self, unidades):
        """Devuelve True si se pudo prestar, False si no alcanza."""
        if unidades <= 0:
            return False
        if unidades > self.disponibles():
            return False
        self.prestados = self.prestados + unidades
        return True

    def devolver(self, unidades):
        if unidades <= 0 or unidades > self.prestados:
            return False
        self.prestados = self.prestados - unidades
        return True

    def estado(self):
        """Semáforo de disponibilidad."""
        libres = self.disponibles()
        if libres == 0:
            return "AGOTADO"
        elif libres <= 2:
            return "POCOS"
        else:
            return "OK"

    def detalle(self):
        """Dato extra de cada tipo. Las hijas lo SOBREESCRIBEN."""
        return "-"

    def ficha(self):
        return (f"{self.icono} [{self.codigo}] {self.nombre:<32} "
                f"{self.disponibles():>2}/{self.cantidad:<2} libres  "
                f"· {self.detalle()}")


# ==============================================================
#  CLASES HIJAS: heredan todo de Componente y agregan lo suyo
# ==============================================================
class Sensor(Componente):
    tipo = "Sensor"
    icono = "📡"

    def __init__(self, codigo, nombre, cantidad, magnitud):
        super().__init__(codigo, nombre, cantidad)
        # (equivale a: Componente.__init__(self, codigo, nombre, cantidad))
        self.magnitud = magnitud      # qué mide: distancia, luz...

    def detalle(self):                # sobreescritura
        return "mide " + self.magnitud


class Actuador(Componente):
    tipo = "Actuador"
    icono = "⚙️"

    def __init__(self, codigo, nombre, cantidad, voltaje):
        super().__init__(codigo, nombre, cantidad)
        self.voltaje = voltaje        # en volts

    def detalle(self):                # sobreescritura
        return f"funciona a {self.voltaje} V"


class Placa(Componente):
    tipo = "Placa"
    icono = "🧠"

    def __init__(self, codigo, nombre, cantidad, pines):
        super().__init__(codigo, nombre, cantidad)
        self.pines = pines            # pines digitales disponibles

    def detalle(self):                # sobreescritura
        return f"{self.pines} pines digitales"

    def prestar(self, unidades):
        # Regla especial: las placas son caras, máximo 1 por préstamo.
        if unidades > 1:
            return False
        return super().prestar(unidades)
