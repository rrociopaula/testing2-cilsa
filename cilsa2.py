def saludar():
    print("¡Hola! Vamos a determinar el tipo de triángulo.")
    
def obtener_lado(mensaje):
    while True:
        try:
            lado = int(input(mensaje))
            if lado > 0:
                return lado
            else:
                print("Error: el valor debe ser un número entero positivo.")
        except ValueError:
            print("Error: por favor, ingresa un número entero válido.")

def determinar_triangulo(lado1, lado2, lado3):
    # Verificamos si es un triángulo válido
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return 3  # Equilátero
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return 1  # Isósceles
        else:
            return 2  # Escaleno
    else:
        return -1  # No es un triángulo válido

def test(lado1, lado2, lado3):
    resultado = determinar_triangulo(lado1, lado2, lado3)
    
    if resultado == -1:
        return 0  # No es un triángulo
    else:
        # Indica el tipo de triángulo y confirma que se ejecutó correctamente
        if resultado == 1:
            print("Es un triángulo isósceles.")
        elif resultado == 2:
            print("Es un triángulo escaleno.")
        elif resultado == 3:
            print("Es un triángulo equilátero.")
        return 1  # Prueba ejecutada correctamente

# Función principal
if __name__ == "__main__":
    saludar()  # Saludamos al usuario
    
    # Solicitamos los lados del triángulo llamando a la función "Obtener lado"
    lado1 = obtener_lado("Ingresa el valor del primer lado: ")
    lado2 = obtener_lado("Ingresa el valor del segundo lado: ")
    lado3 = obtener_lado("Ingresa el valor del tercer lado: ")
    
    # Ejecutamos la prueba
    resultado = test(lado1, lado2, lado3)
    
    if resultado == 0:
        print("Resultado = 0. Error: los lados no forman un triángulo válido.")
    else:
        print("Resultado = 1 .La prueba se ejecutó correctamente.")