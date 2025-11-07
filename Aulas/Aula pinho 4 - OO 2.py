class EMAp: 
    def __new__(cls, *args, **kwargs):
        print("Podemos fazer o que quisermos antes da instância ser criado") #Hook (se meter no fluxo da linguagem de programação)
        object_ = super().__new__(cls)
        print("Podemos fazer o que quisermos depois da instância ser criada") 
        return object_ 


    def __init__(self, nr_alunos):
        print("Podemos fazer o que quisermos antes da instância ser inicializada") 
        self.nr_alunos = nr_alunos
        print("Podemos fazer o que quisermos depois da instância ser inicializada") 
    


escola_nutella = EMAp(42)
print(escola_nutella.nr_alunos)

escola_raiz = object.__new__(EMAp)
escola_raiz.__init__(666)
print(escola_raiz.nr_alunos)