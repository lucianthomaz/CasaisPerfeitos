from enum import Enum
from entrada import Entrada
import pessoa


class Ambiente:
    def __init__(self):
        self.entrada = Entrada('entrada.txt')
        self.entrada.getEntrada()
        self.entrada.getEtnradaSemIndice()
        #self.criarHomens()
        #self.criarMulheres()
        self.criarPopulacao()

    def criarPopulacao(self):
        self.homens = []
        self.mulheres = []
        for i in range(self.entrada.getqtdeCasais()):
            self.homens.append(pessoa.Homem(NomesHomens(i)))
            self.homens[i].setPreferencias(self.entrada.getPreferenciaHomem(i))

        for i in range(self.entrada.getqtdeCasais()):
            self.mulheres.append(pessoa.Mulher(NomesMulheres(i)))
            self.mulheres[i].setPreferencias(self.entrada.getPreferenciaMulher(i))
        
        for row in self.homens:
            row.getPreferencias()

        for row in self.mulheres:
            row.getPreferencias()

class NomesHomens(Enum):
    Joao = 0
    Carlos = 1
    Jose = 2

class NomesMulheres(Enum):
    Maria = 0
    Livia = 1
    Valentina = 2