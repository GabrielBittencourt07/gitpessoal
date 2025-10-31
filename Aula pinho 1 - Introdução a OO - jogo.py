import sys

class guerreiro: 
    def __init__(self, nome):
        self._nome = nome 
        self._arma = None

    def atacar(self):
        if self._arma is not None: 
            print(f"{self._nome} ataca com e causa (10)) ponto(s) de dano")
        else: 
            print(f"{self._nome} ataca com as mãos e causa (1) ponto de dano") 

# class Arma1M: 
#     def __init__(self, nome, dano):
#         self._nome = nome
#         self._dano = dano

#     def __str__(self): 
#         return f"A arma {self._nome} causa {self._dano} pontos de dano"

class feiticeiro: 
    def __init__(self, nome):
        self._nome = nome 
        self._encantamento = None

    def atacar(self):
        if self._encantamento is not None: 
            print(f"{self._nome} lança seu feitiço e causa (10) ponto(s) de dano")
        else: 
            print(f"{self._nome} ataca com as mãos e causa (1) ponto de dano") 

class grupo_de_aventureiros: 
    def __init__(self, nome):
        self._name = nome 
        self._guerreiro = None
        self._feiticeiro = None
    
    def __str__(self): 
        return f"papapapapapa"


#Driver Code
feiticeiro_1 = feiticeiro("Merlin")
guerreiro_1 = guerreiro("Viking")
# arma_1 = Arma1M("Adaga", 7 )
# guerreiro_1._arma = arma_1

guerreiro_1.atacar()
feiticeiro_1.atacar()

guerreiro_1._arma = True
feiticeiro_1._encantamento = True 

guerreiro_1.atacar()
feiticeiro_1.atacar()

grupo_dos_sonhos = grupo_de_aventureiros("Grupo_dos_sonhos")
grupo_dos_sonhos._guerreiro = guerreiro_1 
grupo_dos_sonhos._feiticeiro = feiticeiro_1 
print(grupo_dos_sonhos)


# print("REFERÊNCIAS", sys.getrefcount(arma_1))
# del arma_1
# print("REFERÊNCIAS", sys.getrefcount(guerreiro_1._arma))




