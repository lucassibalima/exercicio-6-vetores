# Criando o vetor
numeros = [0] * 10

# Variáveis
quantidadeNegativos = 0
somaPositivos = 0

# Lendo os números
for i in range(10):
    numeros[i] = float(input(f"Digite o {i+1}º número: "))

# Verificando negativos e somando positivos
for i in range(10):

    if numeros[i] < 0:
        quantidadeNegativos += 1

    if numeros[i] > 0:
        somaPositivos += numeros[i]

# Mostrando os resultados
print("\nVetor:", numeros)
print("Quantidade de números negativos:", quantidadeNegativos)
print("Soma dos números positivos:", somaPositivos)