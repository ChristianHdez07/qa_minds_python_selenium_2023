# Tupla - No se puede modificar
products1 = ("PC", "Laptop", "Tablet", "TV")

# Lista - Se puede modificar
products2 = ["MAC-Laptop", "MAC-Mouse", "ASUS-Laptop", "ASUS-Mouse"]

result = [item for item in products2 if "ASUS" in item]
print(result)
