# -*- coding: utf-8 -*-
"""Python code test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VBzoyCutSQTPK9qccNXOB9oO6DMt5z6a

1.Faça um Programa que leia um número real e imprima o resultado do quadrado desse número.
"""

x = float(input("informe um numero real: "))

quad_num = x*x
print(quad_num)

"""2.Faça um Programa que leia um número real e imprima a quinta parte deste número."""

x = float(input("informe um numero real: "))

quinta_part = x//5
print(quinta_part)

"""3.Faça um Programa que leia um número inteiro e imprima o seu antecessor e o seu sucessor."""

x = int(input("informe um numero inteiro: "))

resultado = x - 1
print(resultado)

x = int(input("informe um numero inteiro: "))

a = x - 1
s = x + 1

print('dado  %  o que antecede é %s e o que sucede é %s.' % (x, a, s))

"""4.Calcule a área de um triângulo, onde leia a medida da base e a medida da altura. Escreva “o triângulo com base... e altura... tem área igual a...”"""

b = float(input("informe o valor da base: "))
a = float(input("informe o valor da altura: "))

x = b * a //2
print(' %f é a area do triangulo com base %f e altura %f.' % (x, b, a))

"""5.Escreva um algoritmo para determinar se um dado número N (recebido através do teclado/ informado pelo usuário) é POSITIVO, NEGATIVO ou NULO."""

num = int(input("informe um numero inteiro: "))

if num >= 0:
  print("número é positivo")
elif num < 0:
  print("número é negativo")
else:
 print("número é invalido")

"""6.Escreva um algoritmo que receba um número e imprima uma das mensagens: “é múltiplo de 3” ou “não é múltiplo de 3”."""

num = int(input("informe um numero inteiro: "))

if num % 3 == 0 :
  print("é multiplo de 3")
elif num % 3 != 0:
  print("não é multiplo de 3")
else:
 print("número é invalido")

"""7.Escreva um algoritmo que leia um número fornecido pelo usuário e informe se ele é ou não divisível por 5."""

num = int(input("informe um numero inteiro: "))

if num % 5 == 0 :
  print("é divisivel por 5")
elif num % 5 != 0:
  print("não é divisivel por 5")
else:
 print("número é invalido")

"""8.Escreva um algoritmo para determinar se um número A é divisível por um outro número B. Esses valores devem ser fornecidos pelo usuário."""

b = int(input("informe um numero inteiro  "))
a = int(input("informe outro numero inteiro: "))


if b % a == 0 :
  print(' %f é divisivel por %f .' % ( b, a))
else:
  print(' %2f não é divisivel por %2f .' % ( b, a))

"""9.Tendo como dados de entrada a altura e o sexo biológico de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
✔ Para homens: (72,7 x h) – 58
✔ Para mulheres: (62,1 x h) – 44,7

"""

altura = float(input('insira sua altura: '))
sexo = input('insira seu sexo com "F" ou "M": ')

'''if sexo == 'F' and (72,1 * altura):
    print('o peso ideal é',)
elif sexo == 'M' and ()'''

#questão 09
if sexo == 'F':
    pesoIdealF = 62.1 * altura
    print(pesoIdealF)
elif sexo == 'M':
    pesoIdealM = 72.1 * altura
    print(pesoIdealM)

"""10.Dados três valores A, B e C, construa um algoritmo, que imprima os valores de forma ascendente (do menor para o maior)."""

a = int(input("informe um numero inteiro: "))
b = int(input("informe um numero inteiro: "))
c = int(input("informe um numero inteiro: "))

list = [a,b,c]

list.sort()

print(list)

"""11.Dados três valores A, B e C, construa um algoritmo, que imprima os valores de forma descendente (do maior para o menor)."""

a = int(input("informe um numero inteiro: "))
b = int(input("informe um numero inteiro: "))
c = int(input("informe um numero inteiro: "))

list = [a,b,c]

list.sort(reverse=True)

print(list)

""" 12.Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 0 até 500."""

soma = 0

for n in range(0, 501,2):
    soma += n

print("Somatório dos valores pares de 0 a 500:", soma)

"""13.Construa um algoritmo que leia um conjunto de dados contendo altura de 50 pessoas, e depois,calcule e escreva a maior e a menor altura."""

n = int(input("informe o total de pessoas cuja altura deseja comparar: "))

maior_altura = float("-inf")
menor_altura = float("inf")

for i in range(n):
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))

    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

print("Maior altura:", maior_altura)
print("Menor altura:", menor_altura)

"""14.Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão contendo seu número de identificação e seu peso. Fazer um algoritmo que escreva o número e peso do boi mais gordo e do boi mais magro."""

boi_gordo = ("", float("-inf"))
boi_magro = ("", float("inf"))

for i in range(90):
    numero_identificacao = input(f"Digite o número de identificação do boi {i+1}: ")
    peso = float(input("Digite o peso do boi: "))

    if peso > boi_gordo[1]:
        boi_gordo = (numero_identificacao, peso)
    if peso < boi_magro[1]:
        boi_magro = (numero_identificacao, peso)

print("Boi + gordo:", boi_gordo)
print("Boi + magro:", boi_magro)

"""18.Desenvolva um programa que armazene quatro notas em uma lista e que apresenta: a média final, a maior nota e a menor nota."""


"""19.Desenvolva um programa que armazene quatro notas em uma lista e que apresenta a média final. Caso a média seja igual ou superior a 7, 
apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. 
Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO""""

print("Digite a primeira nota") #pedindo uma informação ao usuário
nota1 = float(input()) #Convertendo o que foi digitado pelo usuário para real e em seguida salvando na variavel
print("Digite a segunda nota") #pedindo uma informação ao usuário
nota2 = float(input()) #Convertendo o que foi digitado pelo usuário para real e em seguida salvando na variavel
print("Digite a terceira nota") #pedindo uma informação ao usuário
nota3 = float(input())
print("Digite a quarta nota") #pedindo uma informação ao usuário
nota4 = float(input())
media = (nota1 + nota2 + nota3 + nota4)/4 #calculando a média das notas e salvando na variavel media
print("A média foi: %.2f" % media) #mostrando a media com apenas 2 casas decimais
if media >= 7: #verificando se a média é maior ou igual a 7
  print("O aluno foi aprovado") #caso seja, o aluno é aprovado
elif media >= 5: #se a média for menor do que 7, verificamos se ela é maior ou igual a 5
  print("O aluno está na recuperação") #caso seja, o aluno está na recuperação
else: #caso contrário, ou seja, média menor do que 5
  print("O aluno foi reprovado") #o aluno é reprovado

"""28.Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva um programa que encontre todos os pares inversos na lista de palavras."""

def verdadeiro_par_inverso(word1, word2):
    word1_cleaned = ''.join(word1.split()).lower()
    word2_cleaned = ''.join(word2.split()).lower()

    return word1_cleaned == word2_cleaned[::-1]

def encontrar_pares_inversos(lista_palavras):
    pares_inversos = []

    for i in range(len(lista_palavras)):
        for j in range(i+1, len(lista_palavras)):
            if verdadeiro_par_inverso(lista_palavras[i], lista_palavras[j]):
                pares_inversos.append((lista_palavras[i], lista_palavras[j]))

    return pares_inversos

# Solicitar palavras ao usuário
num_palavras = int(input("Quantas palavras você quer inserir? "))
palavras = []
for i in range(num_palavras):
    palavra = input(f"Digite a palavra {i+1}: ")
    palavras.append(palavra)

# Encontrar pares inversos
pares_encontrados = encontrar_pares_inversos(palavras)

# Exibir os pares inversos encontrados
if len(pares_encontrados) > 0:
    print("Pares inversos encontrados:")
    for par in pares_encontrados:
        print(par[0], "-", par[1])
else:
    print("Nenhum par inverso encontrado.")
