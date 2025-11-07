class Guerreiro: 
    def __init__(self, nome):
        self.nome = nome 
        self._arma = None

    def atacar(self): 
        if self._arma is not None:
            print(f"{self.nome} ataca com {self._arma.nome}")
        else: 
            print(f"{self.nome} atacou com as próprias mãos")

    def equipar_arma(self, arma): 
        self._arma = Arma(arma)

    def __del__(self): 
        print(f"Removendo {self.nome}")

class Arma:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        print(f"Eu sou a arma {self.nome}")

    def __del__(self): 
        print(f"Removendo {self.nome}")

#=============================================
guerreiro_1 = Guerreiro("Miyamoto Musashi")
guerreiro_1.atacar()

guerreiro_1.equipar_arma("Wakizashi")
guerreiro_1.atacar()

#Ler o livro dos 5 anéis 
#O guerreiro vive sem a arma, a arma não vive sem o guerreiro 

