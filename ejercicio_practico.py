# --- Funciones de operaciones básicas ---

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

# --- Programa principal ---

def ejecutar_calculadora():
    print("--- CALCULADORA TALENTO LAB ---")
    
    # Manejo de excepciones para entradas que no sean números
    try:
        num1 = float(input("Ingresá el primer número: "))
        num2 = float(input("Ingresá el segundo número: "))
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingresá solo números.")
        return

    print("\nSeleccioná la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Opción (1-4): ").strip()

    if opcion == "1":
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == "2":
        print(f"Resultado: {restar(num1, num2)}")
    elif opcion == "3":
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == "4":
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Error: Opción no válida.")

if __name__ == "__main__":
    ejecutar_calculadora()