class Cuenta:
    def __init__(self):
        self._titular = ""
        self._cantidad = 0.0

    #Métodos

    def set_titular(self,titular):
        self._titular = titular

    """def set_cantidad(self,cantidad):
        if cantidad > 0:
            self.cantidad = cantidad"""

    def get_titular(self):
        return self._titular

    def get_cantidad(self):
        return self.cantidad

    def ingresar(self,cantidad):
        if cantidad >= 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        self._cantidad -= cantidad

    def mostrar(self):
        return f"Titular de la cuenta: {self._titular} \nCantidad disponible en la cuenta: {self._cantidad} $"

x = Cuenta()

titular = str(input("Ingrese nombre del titular de la cuenta: "))
x.set_titular(titular)

ingresar = float(input("¿Cuánto dinero desea ingresar a su cuenta bancaria?: "))
x.ingresar(ingresar)
if ingresar >=0:    
    retirar = str(input("¿Desea retirar dinero? Si-->s No-->n: "))
    if retirar.lower() == "s":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        x.retirar(cantidad)
        print(x.mostrar())
    else:
        print("Fin del programa")

else:
    print("Fin del programa")