# Faça um programa para imprimir o menor elemento de uma lista.

print('Bem vindo ao programa que exibe o menor número de uma lista!')

lista = [5, 9, 7, 10, 1, 65, -74, 65, 87]
menor = lista[0]

print(f'Lista: {lista}')

for e in lista:
    if e < menor:
        menor = e

print(f'\nO menor número é {menor}')
