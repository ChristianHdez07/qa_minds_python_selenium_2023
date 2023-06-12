# Crear la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, numero_cuenta: int, titular_cuenta: str, saldo: float):
        self.__numero_cuenta = numero_cuenta
        self.__titular_cuenta = titular_cuenta
        self.__saldo = saldo

    def depositar(self, dinero: float):
        self.__saldo += dinero
        print("Se han depositado $", dinero, "en la cuenta.")

    def retirar(self, dinero: float):
        if self.__saldo >= dinero:
            self.__saldo -= dinero
            print("Se han retirado $", dinero, "de la cuenta.")
        else:
            print("No hay suficiente saldo en la cuenta para realizar el retiro.")

    def consultar_saldo(self):
        print("El saldo actual de la cuenta es: $", self.__saldo)

# Pedir al usuario que ingrese los datos de la cuenta bancaria
numero_cuenta = input("Ingrese el número de cuenta: ")
titular_cuenta = input("Ingrese el titular de la cuenta: ")
saldo = float(input("Ingrese el saldo inicial de la cuenta: "))

# Crear un objeto cuenta_bancaria a partir de la clase CuentaBancaria
cuenta_bancaria = CuentaBancaria(numero_cuenta, titular_cuenta, saldo)

# Permitir al usuario realizar operaciones bancarias
while True:
    print("\n1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = int(input("Ingrese la opción que desee: "))

    if opcion == 1:
        dinero = float(input("Ingrese el monto de dinero a depositar: "))
        cuenta_bancaria.depositar(dinero)
    elif opcion == 2:
        dinero = float(input("Ingrese el monto de dinero a retirar: "))
        cuenta_bancaria.retirar(dinero)
    elif opcion == 3:
        cuenta_bancaria.consultar_saldo()
    else:
        print("Salir del programa")
        break