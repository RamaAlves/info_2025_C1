class Personaje:
    def __init__(self, nombre, nivel=1, salud=100):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.salud_maxima = salud # Para evitar que se cure por encima del máximo Queremos esto? 
        #lo dejamos por ahora quizas sea una opcion sacarlo o implementar un escudo 
        # que si se cura mas del 100% se carga el escudo

    def presentarse(self):
        print(f"Nombre: {self.nombre}, Nivel: {self.nivel}, Salud: {self.salud}")

    def recibir_danio(self, cantidad):
        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0 #👍
        print(f"{self.nombre} recibió {cantidad} de daño. Salud actual: {self.salud}")

    def curarse(self, cantidad):
        self.salud += cantidad
        if self.salud > self.salud_maxima:
            self.salud = self.salud_maxima #aca se puede implementar lo del escudo, pero como una version 2
            #vamos primero por la solucion al caso planteado
        print(f"{self.nombre} se curó {cantidad} puntos. Salud actual: {self.salud}")

# Probamos
guerrero = Personaje("Ariana", 5, 100)
guerrero.presentarse()
guerrero.recibir_danio(30)
guerrero.curarse(20)
guerrero.recibir_danio(100)
guerrero.presentarse()

class Guerrero(Personaje):
    def atacar(self):
        danio = 5 * self.nivel # 5 danio por defecto
        print(f"{self.nombre} ataca causando {danio} de daño")
        return danio

class Mago(Personaje):
    def __init__(self,nombre,nivel,salud,mana):
        super().__init__(nombre, nivel,salud)
        self.mana= mana

    def lanzar_hechizo(self):
        if self.mana >= 10:
            danio = 15 * self.nivel #daño
            self.mana -=10 #costo 
            print(f"{self.nombre} causa {danio} de daño lanzando un hechizo. Maná restante {self.mana}.")
            return danio 
        else:
            print(f"{self.nombre} no tiene maná suficiente.")


# Probamos
guerrero = Guerrero("Thor", 3, 120)
guerrero.presentarse()
guerrero.recibir_danio(25)
guerrero.curarse(35)
guerrero.presentarse()
guerrero.atacar()
mago = Mago("Merlin", 4, 140,20)
mago.presentarse()
mago.recibir_danio(25)
mago.curarse(35)
mago.presentarse()
mago.lanzar_hechizo()
mago.lanzar_hechizo()
mago.lanzar_hechizo()
mago.lanzar_hechizo()
mago.presentarse()

def combate(pers1, pers2):
    pass

combate(guerrero, mago)