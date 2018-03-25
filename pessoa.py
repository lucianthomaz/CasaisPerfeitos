class Pessoa:
    def __init__(self, name):
        self.name = name        

    def getName(self):
        return self.name

    def setPreferencias(self, preferencias):
        self.preferencia1 = preferencias[0]
        self.preferencia2 = preferencias[1]
        self.preferencia3 = preferencias[2]

class Homem(Pessoa):
    def getPreferencias(self):
        print('Preferencias do', self.name)
        print("Preferencia 1: Mulher", self.preferencia1)
        print("Preferencia 2: Mulher", self.preferencia2)
        print("Preferencia 3: Mulher", self.preferencia3)

class Mulher(Pessoa):
    def getPreferencias(self):
        print('Preferencias da', self.name)
        print("Preferencia 1: Homem", self.preferencia1)
        print("Preferencia 2: Homem", self.preferencia2)
        print("Preferencia 3: Homem", self.preferencia3)