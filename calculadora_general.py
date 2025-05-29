def decimal_to_binary(n):
    return bin(n)[2:]

def decimal_to_hexadecimal(n):
    return hex(n)[2:]

def decimal_to_octal(n):
    return oct(n)[2:]

def binary_to_decimal(b):
    return int(b, 2)

def hexadecimal_to_decimal(h):
    return int(h, 16)

def octal_to_decimal(o):
    return int(o, 8)

def complemento_a_2(binario, bits=8):
    if len(binario) > bits:
        raise ValueError("El número binario excede el número de bits especificado.")
    binario = binario.zfill(bits)
    if binario[0] == '0':
        return binario
    invertido = ''.join('1' if b == '0' else '0' for b in binario)
    suma = bin(int(invertido, 2) + 1)[2:].zfill(bits)
    return suma
if __name__ == "__main__":
    while True:
        print("\n=== Calculadora de Conversiones ===")
        print("0. Salir")
        print("1. Decimal")
        print("2. Binario")
        print("3. Hexadecimal")
        print("4. Octal")
        print("5. Complemento a 2 (binario)")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        elif opcion == "1":
            decimal = int(input("Ingresa un número decimal: "))
            print("Binario:", decimal_to_binary(decimal))
            print("Hexadecimal:", decimal_to_hexadecimal(decimal))
            print("Octal:", decimal_to_octal(decimal))

        elif opcion == "2":
            binario = input("Ingresa un número binario: ")
            print("Decimal:", binary_to_decimal(binario))

        elif opcion == "3":
            hexadecimal = input("Ingresa un número hexadecimal: ")
            print("Decimal:", hexadecimal_to_decimal(hexadecimal))

        elif opcion == "4":
            octal = input("Ingresa un número octal: ")
            print("Decimal:", octal_to_decimal(octal))

        elif opcion == "5":
            binario = input("Ingresa un número binario: ")
            bits = int(input("Cantidad de bits (por defecto 8): ") or "8")
            print("Complemento a 2:", complemento_a_2(binario, bits))

        else:
            print(" Opción no válida. Intenta de nuevo.")