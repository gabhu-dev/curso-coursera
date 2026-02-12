input_value = input('Escribe un numero: ')
print(f'Ingresaste: {input_value}')
number = int(input_value)

# this is my first program in python
if(number % 2 == 0):
    print(f'El número {number} es par')
else:
    print(f'El número {number} es impar')


if number > 2 :
    print('Bigger')
else:
    print('Not bigger')
print('All done')