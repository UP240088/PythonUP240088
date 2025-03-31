#1
import random

def shuffle_list(lista):
    random.shuffle(lista)
    return lista
mi_lista = [1, 2, 3, 4, 5]
print(shuffle_list(mi_lista)) 

#2
import random

def generate_unique_numbers():
    return random.sample(range(10), 7)
print(generate_unique_numbers())