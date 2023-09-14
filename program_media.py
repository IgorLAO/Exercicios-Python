print("Bem vindo a calculadora de media ")
numNotas = int(input("quantas notas ira digitar? "))

i = 0
notas = []

for i in range(numNotas):
    nota = float(input("digite a nota: "))
    notas.append(nota)
    
    
soma = sum(notas)
media = soma / numNotas

print("quantidade de notas" , numNotas)
print("a media do aluno é ", media)