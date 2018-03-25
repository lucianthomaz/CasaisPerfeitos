from entrada import Entrada
import pessoa


class Ambiente:
    def __init__(self):
        self.entrada = Entrada('entrada.txt')
        self.entrada.getEntrada()
        self.entrada.getEtnradaSemIndice()
        self.criarHomens()
        self.criarMulheres()

    def criarHomens(self):
        self.homen1 = pessoa.Homem('Joao')
        self.homen1.setPreferencias(self.entrada.getPreferenciaHomem(2))
        self.homen1.getPreferencias()

    def criarMulheres(self):
        self.mulher1 = pessoa.Mulher('Maria')
        self.mulher1.setPreferencias(self.entrada.getPreferenciaMulher(2))
        self.mulher1.getPreferencias()
