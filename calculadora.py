#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def porcentaje(numero, tasa):
    return numero * tasa / 100

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

def main():
    print("Calculadora sencilla")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Calcular porcentaje")
    
    try:
        opcion = input("Seleccione una opción (1-5): ")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == "1":
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {dividir(num1, num2)}")
        elif opcion == "5":
            print(f"Resultado: {porcentaje(num1, num2)}")
        else:
            print("Opción inválida")
    except ValueError:
        print("Error: Debe ingresar números válidos")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
