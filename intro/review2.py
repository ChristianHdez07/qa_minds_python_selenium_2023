# Crear una lista vacía para almacenar las personas
persons = []

# Utilizar un bucle while para permitir al usuario ingresar la información de cada persona
while True:
    # Pedir al usuario que ingrese el nombre, la edad y la ciudad de residencia de la persona
    name = input("Ingrese el nombre de la persona: ")
    age = input("Ingrese la edad de la persona: ")
    city = input("Ingrese la ciudad de residencia de la persona: ")

    # Crear un diccionario con la información de la persona
    person = {"nombre": name, "edad": age, "ciudad": city}

    # Agregar el diccionario de la persona a la lista de personas
    persons.append(person)

    # Preguntar al usuario si desea ingresar la información de otra persona
    answer = input("¿Desea ingresar la información de otra persona? (s/n)")
    if answer.lower() != "s":
        break

# Mostrar la información completa de todas las personas ingresadas
for persona in persons:
    print()
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    print("Ciudad de residencia:", persona["ciudad"])
