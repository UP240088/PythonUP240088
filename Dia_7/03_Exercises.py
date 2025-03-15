age = [22, 19, 24, 25, 26, 24, 25, 24]
#1.
st = set(age)
print(len(st))
print(len(age))
#2
#Cadena de texto (String): Secuencia de caracteres, inmutable, ordenada, permite duplicados. Ejemplo: 'hola'.
#Lista (List): Colección mutable, ordenada, permite duplicados. Ejemplo: [1, 2, 3].
#Tupla (Tuple): Colección inmutable, ordenada, permite duplicados. Ejemplo: (1, 2, 3).
#Conjunto (Set): Colección mutable, desordenada, no permite duplicados. Ejemplo: {1, 2, 3}.
#3.
sentence = "I am a teacher and I love to inspire and teach people"
word = set(sentence.split())
print(len(word))