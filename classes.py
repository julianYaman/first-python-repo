class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

hoth = Planet('Hoth', 200000, 5.5, "Hoth System")
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius} ')
print(f'The gravity is: {hoth.gravity} ')
print(hoth.orbit())

naboo = Planet("Naboo", 300000, 8, "Naboo Sytem")
print(f'Name is: {naboo.name}')
print(f'Radius is: {naboo.radius} ')
print(f'The gravity is: {naboo.gravity} ')
print(naboo.orbit())

