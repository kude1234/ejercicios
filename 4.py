n = int(input("Ingresa n (total de elementos): "))
r = int(input("Ingresa r (elementos que eliges, con repetición): "))

if n <= 0:
 print("n debe ser mayor que 0.")
elif r < 0:
 print("r debe ser mayor o igual a 0.")
else:
# Cálculo: VR(n, r) = n^r
 resultado = 1
for i in range(r):
 resultado *= n
print(f"VR({n}, {r}) = {resultado}")