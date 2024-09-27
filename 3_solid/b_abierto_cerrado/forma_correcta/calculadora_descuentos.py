from descuentos import *

class CalculadoraDescuentos:
    def __init__(self):
        self.descuentos = {
            "estudiante": DescuentoEstudiante(),
            "jubilado": DescuentoJubilado(),
            "empleado": DescuentoEmpleado(),
            "veterano": DescuentoVeterano(),
        }

    def calcular_descuento(self, cliente):
        descuento = self.descuentos.get(cliente.tipo, SinDescuento())
        return descuento.calcular(cliente.total_compra)
