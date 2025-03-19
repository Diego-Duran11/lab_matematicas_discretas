def binario_a_decimal(bin_str: str) -> int:
    return int(bin_str, 2)

def decimal_a_binario(num: int) -> str:
    return bin(num)[2:]

def operaciones_binarias(a: str, b: str, operacion: str) -> str:
    a_dec, b_dec = binario_a_decimal(a), binario_a_decimal(b)
    resultado = {
        'suma': a_dec + b_dec,
        'resta': a_dec - b_dec,
        'multiplicacion': a_dec * b_dec,
        'division': a_dec // b_dec if b_dec != 0 else 'Error: División por cero'
    }.get(operacion, 'Operación no válida')
    return decimal_a_binario(resultado) if isinstance(resultado, int) else resultado

def convertir():
    while True:
        opcion = input("Elija una opción: \n1. Decimal a Binario \n2. Binario a Decimal \n3. Salir\nOpción: ")
        
        if opcion == "1":
            num = int(input("Ingrese un número decimal: "))
            print(f"Binario: {decimal_a_binario(num)}")
        elif opcion == "2":
            bin_str = input("Ingrese un número binario: ")
            print(f"Decimal: {binario_a_decimal(bin_str)}")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")
if __name__ == "__main__":
    convertir()
