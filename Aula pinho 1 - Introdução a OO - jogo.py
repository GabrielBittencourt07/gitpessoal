import sys

class guerreiro: 
    def __init__(self, nome):
        self._nome = nome 
        self._arma = None

    def atacar(self):
        if self._arma is not None: 
            print(f"{self._nome} ataca com {self._arma._nome} e causa {self._arma._dano} ponto(s) de dano")
        else: 
            print(f"{self._nome} ataca com as mãos e causa (1) ponto de dano") 

class Arma1M: 
    def __init__(self, nome, dano):
        self._nome = nome
        self._dano = dano

    def __str__(self): 
        return f"A arma {self._nome} causa {self._dano} pontos de dano"
    

#Driver Code
guerreiro_1 = guerreiro("Viking")
arma_1 = Arma1M("Adaga", 7 )
guerreiro_1._arma = arma_1

guerreiro_1.atacar()

del guerreiro_1

print(arma_1)