# Criando o vetor
notas = [0] * 15

# Variável para soma das notas
soma = 0

# Lendo as notas dos alunos
for i in range(15):
    notas[i] = float(input(f"Digite a nota do {i+1}º aluno: "))
    soma += notas[i]

# Calculando a média
media = soma / 15

# Mostrando os resultados
print("\nNotas dos alunos:", notas)
print("Média geral:", media)