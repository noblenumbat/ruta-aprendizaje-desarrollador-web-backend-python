class PagosEmpleados:
    
    def __init__(self, nombre, pago, valor) -> None:
        self.nombre = nombre
        self.pago = pago 
        self.valor = valor 

    def efectuar_pago(self):
        self.pago = "si"

    def actualizar_estado(self):
        if self.pago == "si":
            return self.nombre + " pago efectuado " + str(self.valor)
        else:
            return self.nombre + " por pagar."

jonathan = PagosEmpleados("Jonathan", "no", 20000)
thalia = PagosEmpleados("Thalia", "no", 30000)
print(jonathan.actualizar_estado(), "\n", thalia.actualizar_estado())
print("Despues del pago")
jonathan.efectuar_pago()
print(jonathan.actualizar_estado(), "\n", thalia.actualizar_estado())