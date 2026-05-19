# Criando o vetor
valores = [0] * 5

# Lendo os valores
for i in range(5):
    valores[i] = float(input(f"Digite o {i+1}º valor: "))

# Considerando o primeiro valor como maior e menor
maior = valores[0]
menor = valores[0]

# Guardando as posições
posMaior = 0
posMenor = 0

# Verificando maior e menor valor
for i in range(5):

    if valores[i] > maior:
        maior = valores[i]
        posMaior = i

    if valores[i] < menor:
        menor = valores[i]
        posMenor = i

# Mostrando os resultados
print("\nValores:", valores)
print("Maior valor:", maior)
print("Posição do maior valor:", posMaior)

print("Menor valor:", menor)
print("Posição do menor valor:", posMenor)