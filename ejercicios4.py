# ej6_combinacion.py
# Programa: combinación C(n, k)

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (elementos que eliges): "))

if 0 <= k <= n:
    C = factorial(n) // (factorial(k) * factorial(n - k))
    print(f"C({n}, {k}) = {C}")
else:
    print("Error: k debe estar entre 0 y n.")
