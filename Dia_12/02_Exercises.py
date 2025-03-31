#1
import random

def list_of_hexa_colors(num_colors):
    hex_chars = '0123456789abcdef'
    hex_colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        hex_colors.append(color)
    
    return hex_colors
print(list_of_hexa_colors(5))

#2
import random

def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append((r, g, b))
    
    return rgb_colors

print(list_of_rgb_colors(5))

#3
import random

def generate_colors(tipo_color, num_colores):
    
    def generar_color_hexa():
        caracteres_hex = '0123456789abcdef'
        return '#' + ''.join(random.choice(caracteres_hex) for _ in range(6))
    
    def generar_color_rgb():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f'rgb({r},{g},{b})'

    colores = []
    for _ in range(num_colores):
        if tipo_color == 'hexa':
            colores.append(generar_color_hexa())
        elif tipo_color == 'rgb':
            colores.append(generar_color_rgb())
        else:
            raise ValueError("Tipo de color no válido. Usa 'hexa' o 'rgb'.")

    return colores

print(generate_colors('hexa', 3)) 
print(generate_colors('rgb', 3))   
