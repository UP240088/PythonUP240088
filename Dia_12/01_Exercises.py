#1
import random
import string

def generate_random_user_id():
    
    random_user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return random_user_id

print(generate_random_user_id())

#2
import random

def user_id_gen_by_user():
   
    num_caracteres = int(input("Ingrese el número de caracteres para el ID: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    ids_generados = []
    
    for _ in range(num_ids):
        id_usuario = ''
        for _ in range(num_caracteres):
            id_usuario += caracteres[random.randint(0, len(caracteres) - 1)]
        ids_generados.append(id_usuario)
    
    return '\n'.join(ids_generados)

print(user_id_gen_by_user())
print(user_id_gen_by_user())  

#3
import random

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())

