# Pedir al usuario que ingrese una lista de números enteros
numbers = input("Ingrese una lista de números enteros separados por comas: ")
list_numbers = numbers.split(",")
list_numbers = [int(num) for num in list_numbers]

# Calcular la suma, el máximo y el mínimo
suma = 0
maximum = list_numbers[0]
minimo = list_numbers[0]
for num in list_numbers:
    suma += num
    if num > maximum:
        maximum = num
    if num < minimo:
        minimo = num

# Mostrar los resultados por pantalla
print(f"La suma de los números es: {suma}")
print("El número máximo es:", maximum)
print("El número mínimo es:", minimo)
