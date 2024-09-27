from descuento_base import DescuentoBase

class SinDescuento(DescuentoBase):
    def calcular(self, total_compra):
        return total_compra  # Sin descuento

class DescuentoEstudiante(DescuentoBase):
    def calcular(self, total_compra):
        return total_compra * 0.8  # 20% de descuento

class DescuentoJubilado(DescuentoBase):
    def calcular(self, total_compra):
        return total_compra * 0.85  # 15% de descuento
    
class DescuentoEmpleado(DescuentoBase):
    def calcular(self, total_compra):
        return total_compra * 0.9  # 10% de descuento
    
class DescuentoVeterano(DescuentoBase):
    def calcular(self, total_compra):
        return total_compra * 0.88  # 12% de descuento