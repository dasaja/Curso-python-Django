for n in [1,2,3,4,5]:
    m=n**2
    print(n,m)

for n in [1,2,3,4,5]:
    m=n**2
    print(n, m)

for p in ["Guayas", "Los Rios", "Manabí", "Sta. Elena", "Esmeraldas"]:

    print("Provincia", p)

"""for p in ['Guayas', 'Los Rios', 'Manabi','Sta. Elena','Esmeraldas']:
    print('Provincia: ', p)"""



#Generador de contrasenas
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Bienvenido a mi PyPaswword Generator!")
nr_letters = int(input("Cuantas letras quieres en tu contrasena?\n"))
nr_symbols = int(input('Cuantos simbolos quieres?\n'))
nr_numbers = int(input('Cuantos numeros quieres?\n'))

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Tu contrasena es: {password}") 

