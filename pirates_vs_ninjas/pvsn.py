import random

class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def atacar(self, enemigo):
        pass

    def recibir_ataque(self, ataque):
        self.salud -= ataque
        print(f"{self.nombre} recibió {ataque} de daño.")
        if self.salud <= 0:
            print(f"{self.nombre} ha sido derrotado.")

class Ninja(Personaje):
    multiplicador_ataque = 1.5

    @classmethod
    def ataque_rapido(cls, enemigo):
        ataque = random.randint(10, 20) * cls.multiplicador_ataque
        enemigo.recibir_ataque(ataque)
        print(f"{cls.__name__} usó un ataque rápido y causó {ataque} de daño.")

    @staticmethod
    def ninjutsu(enemigo):
        ataque = random.randint(20, 30)
        enemigo.recibir_ataque(ataque)
        print(f"{Ninja.__name__} usó Ninjutsu y causó {ataque} de daño.")

    def atacar(self, enemigo):
        opciones_ataque = [self.ataque_rapido, self.ninjutsu]
        ataque_elegido = random.choice(opciones_ataque)
        ataque_elegido(enemigo)

class Pirata(Personaje):
    multiplicador_ataque = 1.2

    @classmethod
    def trabuco(cls, enemigo):
        ataque = random.randint(15, 25) * cls.multiplicador_ataque
        enemigo.recibir_ataque(ataque)
        print(f"{cls.__name__} usó trabuco y causó {ataque} de daño.")

    @staticmethod
    def sable(enemigo):
        ataque = random.randint(25, 35)
        enemigo.recibir_ataque(ataque)
        print(f"{Pirata.__name__} usó sable y causó {ataque} de daño.")

    def atacar(self, enemigo):
        opciones_ataque = [self.trabuco, self.garfio]
        ataque_elegido = random.choice(opciones_ataque)
        ataque_elegido(enemigo)


ninja = Ninja("Hattori Hanzo", 100)
pirata = Pirata("Jack Sparrow", 100)


while ninja.salud > 0 and pirata.salud > 0:
    print(f"\n{ninja.nombre} ({ninja.salud} salud) vs {pirata.nombre} ({pirata.salud} salud)")
    ninja.atacar(pirata)
    if pirata.salud <= 0:
        break
    pirata.atacar(ninja)

print("\nFin de la batalla.")
