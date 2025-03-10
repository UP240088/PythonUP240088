#1
first_word = 'Thirty'
second_word = 'Days'
third_word = 'of'
fourth_word = 'Python'
space = ' '
single_string = first_word + space + second_word + space + third_word  + space  + fourth_word
print(single_string)
#2
first_word = 'Coding'
second_word = 'For'
third_word = 'All'
space = ' '
single_string = first_word + space + second_word + space + third_word
print(single_string)
#3
company = 'Coding For All'
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
first_word = company [0:6]
print(first_word)
#10
texto = "Coding For All"
posicion = texto.index("Coding" )
print(posicion)
#11
texto = "Coding For All"
try:
    posicion = texto.index("Python")
    print(posicion)
except ValueError:
    print("No fue encontrada.")
#12
print(company.replace('Coding', 'Python'))
#13
print(company.split())
#14
tex1 ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tex1.split())
#15
print(company[0])
#16
print(company.find('l'))
#17
character10 = company [10]
print(character10)
#18
Python_For_Everyone = 'PFE'
print(Python_For_Everyone)
#19
Coding_For_All = 'CFA'
print(Coding_For_All)
#20
print(texto.index('C'))
#21
print(texto.index('F'))
#22
texto6 = 'Coding For All People'
print(texto.rfind('l'))
#23
texto7 = 'You cannot end a sentence with because because because is a conjunction'
print(texto7.index('because'))
#24
print(texto7.rindex('because'))
#25
frase_a_remover = 'because because because'
frase_modificada = texto7.replace(frase_a_remover,"")
print(frase_modificada)
#26
print(texto7.index('because'))
#27
frase_a_remover = 'because because because'
frase_modificada = texto7.replace(frase_a_remover,"")
print(frase_modificada)
#28
Palabra = "Coding"
if texto.startswith(Palabra):
     print("Si, la cadena empieza con 'Coding'")
else:
    print("No, la cadena no empieza con 'Coding'")     
#29
Palabra2 = "coding"
if texto.endswith(Palabra2):
     print("Si, la cadena termina con 'coding'")
else:
    print("No, la cadena no termina con 'coding'")
#30
texto5 = '  Coding For All  '
frase_sin_espacios = texto5.strip()
print(f"Despues de eliminar los espacios: '{frase_sin_espacios}'")    
#31
primera_frase = '30DaysOfPython'
segunda_frase = 'thirty_days_of_python'
print(primera_frase.isidentifier())
print(segunda_frase.isidentifier())
#32
libreria = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = ' # '.join(libreria)
print(resultado)
#33
oraciones = 'I am enjoying this challenge\nI just wonder what is next.'
print(oraciones)
#34
print("Name     \tAge   \tCountry   \tCity")
print("Asabeneh \t250   \tFinland    \tHelsinki")
#35
radio2 = 10
area2 = 3.14 * radio2 ** 2
print(f"El radio es {radio2} y el area es {area2} metros .")

#36
a, b = 8, 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
