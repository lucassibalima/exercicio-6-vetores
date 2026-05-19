# Criando os vetores
numeros = [0] * 10
quadrados = [0] * 10

# Lendo os números reais
for i in range(10):
    numeros[i] = float(input(f"Digite o {i+1}º número: "))

# Calculando o quadrado de cada número
for i in range(10):
    quadrados[i] = numeros[i] ** 2

# Mostrando os vetores
print("\nVetor original:")
for i in range(10):
    print(numeros[i])

print("\nVetor com os quadrados:")
for i in range(10):
    print(quadrados[i])