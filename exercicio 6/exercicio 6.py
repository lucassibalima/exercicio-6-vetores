# Criando o vetor
vetor = [0] * 10

# Lendo os valores do vetor
for i in range(10):
    vetor[i] = int(input(f"Digite o {i+1}º valor: "))

# Considerando o primeiro valor como maior e menor
maior = vetor[0]
menor = vetor[0]

# Verificando maior e menor valor
for i in range(10):
    if vetor[i] > maior:
        maior = vetor[i]

    if vetor[i] < menor:
        menor = vetor[i]

# Mostrando os resultados
print("\nVetor:", vetor)
print("Maior valor:", maior)
print("Menor valor:", menor)