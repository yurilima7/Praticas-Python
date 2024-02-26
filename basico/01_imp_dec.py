# IMPERATIVO | ESTRUTURADO
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for number in numbers:
    if (number % 2 == 0):
        even_numbers.append(number)

print(even_numbers)

# DECLARATIVO | FUNCIONAL
even_numbers_dec = []
even_numbers_dec = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers_dec)

print(''' 
      Olá Python!
      tudo bem com você?
''')