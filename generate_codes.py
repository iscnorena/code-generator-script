import random
import string

def generate_codes(num_codes, file_name):
    # Definir los caracteres permitidos
    allowed_characters = ''.join([char for char in string.ascii_uppercase + string.digits 
                                  if char not in "AEIOU156780GÑQSTOKUVB"])
    
    with open(file_name, 'w') as file:
        for _ in range(num_codes):
            # Generar un código de 12 caracteres de los permitidos
            code = ''.join(random.choice(allowed_characters) for _ in range(12))
            # Escribir cada código en una línea en el archivo
            print(f"{code},A,false")
            file.write(f"{code},A,false\n")

# Llamada a la función para generar los códigos
generate_codes(1000, 'codes.txt')
