def fn_suma(a, b):
    total_suma = a + b
    return total_suma

if __name__ == "__main__":
    # Ejemplo de uso de la función
    a = input('ingrese un numero ')
    b = input('ingrese otro numero ')
    resultado = fn_suma(int(a), int(b))  # Aquí puedes pasar los valores que desees
    print("La suma es:", resultado)

# Crear funcion multiplicar
def fn_multiplicar(a,b):
    total_mult = a*b
    return total_mult
if __name__ == "__main__":
    # Ejemplo de uso de la funcion
    resultado = fn_multiplicar(int(a), int(b)) # Aqui puedes pasar los valores que desee
    print("La multiplicacion es:", resultado)
    