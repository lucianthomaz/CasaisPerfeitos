class Entrada:

    def __init__(self, name):
        self.name = name
        self.lerArquivo()

    def lerArquivo(self):
        with open(self.name, 'r') as f:
            self.qtdeCasais, self.cartorios = [int(x) for x in next(f).split()]  # read first line
            self.entrada = []
            self.entradaSemIndice = []
            for line in f:  # read rest of lines
                self.entrada.append([int(x) for x in line.split()])                
            for row in self.entrada:
                self.entradaSemIndice.append(list(row))
            for row in self.entradaSemIndice:
                row.pop(0)            

    def getEntrada(self):
        print(self.entrada)

    def getEtnradaSemIndice(self):
        print(self.entradaSemIndice)

    def getqtdeCasais(self):        
        return self.qtdeCasais 

    def getCartorios(self):
        return self.cartorios

    def getPreferenciaHomem(self, index=-1):      
        self.prefHomens = []
        if index == -1:
            for i in range(self.qtdeCasais):
                self.prefHomens.append(self.entrada[i])            
            return self.prefHomens
        else:            
            return self.entradaSemIndice[index]

    def getPreferenciaMulher(self, index=-1):
        self.prefMulheres = []
        if index == -1:
            for i in range(self.getqtdeCasais(), self.getqtdeCasais()*2):            
                self.prefMulheres.append(self.entrada[i])
            return self.prefMulheres            
        else:            
            return self.entradaSemIndice[index+self.getqtdeCasais()]
