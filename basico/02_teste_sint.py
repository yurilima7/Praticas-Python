# Teste Sintaxe

# Função
def avaliacao(materia, nota):
    if materia == 'Tecnologia da Informação':
        nivel = 'fácil'
    elif materia[0:6] == 'Direito':
        nivel = 'médio'
    else:
        nivel = 'difícil'

    print('A disciplina ' + materia + ' é ' + nivel)

    # Tratamento de exceção
    try:
        arquivo = open('notasMaterias.txt', 'a')
    except:
        print('Não foi possivel abrir arquivos de notas')
    else:
        arquivo.write(materia + " - " + nota + "\n")

# Saída
print('Digite o nome da disciplina:')

# Entrada
disciplina = input()

print('Digite anota que deseja dar para a disciplina:')
nota = input()

while disciplina != '' and nota != '':
    avaliacao(disciplina, nota)

    print('Digite o nome da disciplina:')

    disciplina = input()

    print('Digite anota que deseja dar para a disciplina:')
    nota = input()