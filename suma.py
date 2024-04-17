matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
  for j in range(3):
    matriz[i][j] = int(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))
suma = 0
for i in range(3):
  for j in range(3):
    suma += matriz[i][j]

print("\nMatriz:")
for i in range(3):
  for j in range(3):
    print(f"{matriz[i][j]:2}", end=" ")
  print()
print(f"\nSumatoria de los elementos: {suma}")