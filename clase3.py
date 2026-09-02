try:
    valor = int(input("Ingresa un número entero: "))
    resultado = 10 / valor
    print(f"10 / {valor} = {resultado}")
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Entrada inválida, no es un número entero.")
finally:
    print("Operación finalizada.")