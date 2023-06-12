directory = {
    "Alexis": "1234567",
    "Melisa": "0123456",
    "Christian": "9876541"
}

print(directory)
print(directory.get("Alexis"))

for key, val in directory.items():
    print(f"{key} - {val}")