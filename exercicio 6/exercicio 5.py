# Criando o vetor
vetor = [0] * 10

# Contador de números pares
pares = 0

# Lendo os valores do vetor
for i in range(10):
    vetor[i] = int(input(f"Digite o {i+1}º valor: "))

# Verificando quantos valores são pares
for i in range(10):
    if vetor[i] % 2 == 0:
        pares += 1

# Mostrando o resultado
print("\nVetor:", vetor)
print("Quantidade de valores pares:", pares)