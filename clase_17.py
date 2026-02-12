import random
from random import Random

# CICLO DE VIDA DE OBJETOS
class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(f'Construyendo {self.name}')

    def party(self):
        self.x = self.x + 1
        print(f'Fiesta {self.name} {self.x}')

    def __del__(self):
        print(f'{self.name} se va de la fiesta')

an = PartyAnimal('Sally') # instaciarlo
an.party()
an.party()

class FootballFan(PartyAnimal):
    points = 0
    def __init__(self, z):
        super().__init__(z)
        self.points = 0
        print(f'Construyendo FootballFan {self.name}')

    def __touchdown(self):
        self.points = self.points + 7
        self.party()
        print(f'Gooaaal! {self.name} tiene {self.points} puntos!')


class User:
    total_logins = 0 # variable de clase compartida por todas las instancias
    def __init__(self, username):
        self.username = username
        self.logged_in = False
        self.__password = '' # Privado
        self._id = 0       # Protegido

    def login(self, password):
        # Simulate password check
        if password == 'secret':
            self.logged_in = True
            self.__password = password
            self._id += Random().randint(1, 1000)
            User.total_logins += 1
            print(f'User {self.username} logged in successfully.')
        else:
            print('Login failed!')

    def logout(self):
        self.logged_in = False
        print(f'User {self.username} logged out.')

user1 = User('alice')
user1.login('secret')
# print(dir(user1))
print(user1._User__password) # Se puede acceder, pero no es recomendable, no hay una visibilidad real de privado en Python, solo es una convención.
print(user1._id) # Acceso a variable protegida, pero no es recomendable hacerlo desde fuera de la clase.

