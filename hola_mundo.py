# Mi primer programa en Python
def saludar(nombre):
    """Función que saluda a una persona"""
    return f"¡Hola, {nombre}! Bienvenido a Python."
if __name__ == "__main__":
    nombre = input("¿Cuál es tu nombre? ")
mensaje = saludar(nombre)
print(mensaje)
print(f"Python es genial para programar.") 