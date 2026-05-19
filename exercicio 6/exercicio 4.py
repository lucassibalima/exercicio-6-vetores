# Criando o vetor com 8 posições
vetor = [0] * 8

# Lendo os valores do vetor
for i in range(8):
    vetor[i] = int(input(f"Digite o valor da posição {i}: "))

# Lendo as posições X e Y
X = int(input("\nDigite a posição X: "))
Y = int(input("Digite a posição Y: "))

# Calculando a soma
soma = vetor[X] + vetor[Y]

# Mostrando o resultado
print("\nVetor:", vetor)
print("Soma dos valores nas posições", X, "e", Y, "=", soma)