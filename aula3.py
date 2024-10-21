continuar = 'sim'
while continuar.lower() == 'sim':
    numero = int(input('Digite um número: '))

    if numero % 3 == 0 and numero % 5 == 0:
        print('Fizzbuzz')
    elif numero % 3 == 0:
        print('Fizz')
    elif numero % 5 == 0:
        print('Buzz')
    else:
        print('Número não é divisível por 3 ou 5.')

    continuar = input('Deseja continuar? (sim/não): ')

palavras = ['Filipe','16 anos','2 Ano do Ensino Médio']
len(palavras)

print('Aluno:')
for palavras in palavras:
    print(palavras)



# ATIVIDADE PRÁTICA 2

# Faça um programa que leia 3 números e informe o

# maior número e o menor.


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


maior_numero = max(num1, num2, num3)
menor_numero = min(num1, num2, num3)

print("O maior número é:", maior_numero)
print("O menor número é:", menor_numero)



