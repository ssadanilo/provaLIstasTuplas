# Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. 
# Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. 
# Por fim, exiba na tela os números pares, os números ímpares em uma tupla, 
# a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.


# Criando lista de números pares e ímpares

paresLista = []
imparesLista = []

# Usando o laço for para separar os inputs de números pares e ímpares em suas respectivas listas

for i in range(10):
    digite_numero = int(input(f'Digite um númro {i + 1}: '))
    if digite_numero % 2 != 0:
        imparesLista.append(digite_numero)
    else:
        paresLista.append(digite_numero)

# Transformando a lista de números impares em uma tupla

tuplaImparesLista = tuple(imparesLista)

# Somando as listas dos pares e impares em uma única lista        

paresImparesLista = paresLista + imparesLista

print(f'Lista de números pares: {paresLista}')
print(f'Tupla de números impares: {tuplaImparesLista}')
print(f'Quantidade de números pares: {len(paresLista)}')
print(f'A quantidade de números pares e impares: {len(imparesLista)}')
print(f'A somas de tdos os números pares e ímpares: {sum(paresImparesLista)}')
