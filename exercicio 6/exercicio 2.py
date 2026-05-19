# Criando o vetor
valores = [0, 0, 0, 0, 0, 0]

# Lendo os 6 valores inteiros
for i in range(6):
    valores[i] = int(input(f"Digite o {i+1}º valor: "))

# Mostrando os valores lidos
print("\nValores digitados:")

for i in range(6):
    print(valores[i])
    