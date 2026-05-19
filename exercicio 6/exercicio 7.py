# Criando o vetor
vetor = [0] * 10

# Lendo os valores
for i in range(10):
    vetor[i] = int(input(f"Digite o {i+1}º valor: "))

# Considerando o primeiro elemento como maior
maior = vetor[0]
posicao = 0

# Verificando o maior valor e sua posição
for i in range(10):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i

# Mostrando os resultados
print("\nVetor:", vetor)
print("Maior elemento:", maior)
print("Posição do maior elemento:", posicao)
