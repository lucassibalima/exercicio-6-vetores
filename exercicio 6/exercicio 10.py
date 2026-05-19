# Criando o vetor
valores = [0] * 5

# Variável para soma
soma = 0

# Lendo os valores
for i in range(5):
    valores[i] = float(input(f"Digite o {i+1}º valor: "))
    soma += valores[i]

# Considerando o primeiro valor como maior e menor
maior = valores[0]
menor = valores[0]

# Verificando maior e menor valor
for i in range(5):

    if valores[i] > maior:
        maior = valores[i]

    if valores[i] < menor:
        menor = valores[i]

# Calculando a média
media = soma / 5

# Mostrando os resultados
print("\nValores lidos:", valores)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média dos valores:", media)