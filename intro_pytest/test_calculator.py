class Calculadora:
    def __init__(self):
        pass

    def suma(self, num_a: int, num_b: int):
        return num_a + num_b

    def resta(self, num_a: int, num_b: int):
        return num_a - num_b

    def multiplicacion(self, num_a: int, num_b: int):
        return num_a ** num_b

    def division(self, num_a: int, num_b: int):
        return num_a / num_b

def test_suma():
    calc = Calculadora()
    result = calc.suma(7, 10)
    assert result == 17
    print(f"Suma: {result}")

def test_resta():
    calc = Calculadora()
    result = calc.resta(9, 2)
    assert result == 7
    print(f"Resta: {result}")

def test_multiplicacion():
    calc = Calculadora()
    result = calc.multiplicacion(5, 2)
    assert result == 25
    print(f"Multiplicación: {result}")

def test_division():
    calc = Calculadora()
    result = calc.division(9, 3)
    assert result == 3
    print(f"Division: {result}")
