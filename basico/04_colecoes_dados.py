# Listas: coleção de valores organizada por índice (iniciado sempre por 0). São mutáveis, podendo ser alteradas após a sua criação.
print('-------------- Listas --------------')
listPessoas = ['Jack Cruz', 'Maria']
print('Lista Pessoas: ' + str(listPessoas))
print(listPessoas[0])

# Tuplas: coleção de valores com características semelhantes às das listas, porém são imutáveis.
print('\n-------------- Tuplas --------------')
signos = ("Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes")
print(signos[4])

# Sets: coleção de valores não ordenados e não duplicados. Da mesma forma que as listas, também são mutáveis.
print('\n-------------- Sets --------------')
pessoas = {"Santos", "Paula", "Caio", "Lara", "Diego"}
print('Set Pessoas: ' + str(pessoas))

# Dicionários: coleção em que cada elemento é representado pelo par “chave:valor”
print('\n-------------- Dicionários --------------')
dictPessoa = {"nome": "Santos", "altura": 1.76}
print(dictPessoa['nome'])
print(dictPessoa['altura'])

# ------ MANIPULANDO ------
print('\n\n-------------- MANIPULANDO --------------')
# LISTA
print('\n-------------- Listas --------------')
# Adicionando elemento no final
listPessoas.append('Caio')
listPessoas.append('Joana')
print('Lista Pessoas: ' + str(listPessoas))

# Inserindo elemento em uma determinada posição
listPessoas.insert(0, "Alário")
print('Lista Pessoas: ' + str(listPessoas))

# Removendo um elemento da lista
listPessoas.remove('Jack Cruz')
print('Lista Pessoas: ' + str(listPessoas))

# Removendo um elemento da lista com base na posição
listPessoas.pop(2)
print('Lista Pessoas: ' + str(listPessoas))

# SET
print('\n-------------- Set --------------')
# Insereindo elemento no set
pessoas.add("Marina")
print('Set Pessoas: ' +  str(pessoas))

# Removendo um elemento do conjunto
pessoas.remove('Santos')
print('Set Pessoas: ' +  str(pessoas))

# União dos conjuntos
pessoasB = {'Marta', 'Mário', 'Laura', 'Orlando', 'Paula'}
print('Set Pessoas - união: ' + str(pessoas | pessoasB))

# Intersecção de conjuntos - tem em ambos
print('Set Pessoas - intersecção: ' + str(pessoas & pessoasB))

# Diferença de conjuntos
print('Set Pessoas - diferença 1: ' + str(pessoas - pessoasB))
print('Set Pessoas - diferença 2: ' + str(pessoasB - pessoas))

# Diferença simétrica de conjuntos - ignora o que tem de igual (Intersecção)
print('Set Pessoas - diferença simétrica 1: ' + str(pessoas ^ pessoasB))
print('Set Pessoas - diferença simétrica 2: ' + str(pessoasB ^ pessoas))

# DICIONÁRIO
print('\n-------------- Dicionário --------------')
# Acesso a um elemento do dicionário
print(dictPessoa.get("nome", "Nome não encontrado"))

# Adicionando um elemento ao dicionário
dictPessoa.update({"idade": 23})
print(dictPessoa.get("idade", "Idade não encontrada"))

# Removendo um elemento
dictPessoa.pop("altura")
print(dictPessoa.get('altura', 'Altura não encontrada'))