class CalculadoraDescuentos:
    def calcular_descuento(self, cliente):
        if cliente.tipo == "estudiante":
            return cliente.total_compra * 0.8  # 20% de descuento
        elif cliente.tipo == "jubilado":
            return cliente.total_compra * 0.85  # 15% de descuento
        elif cliente.tipo == "empleado":
            return cliente.total_compra * 0.9  # 10% de descuento
        else:
            return cliente.total_compra  # Sin descuento
