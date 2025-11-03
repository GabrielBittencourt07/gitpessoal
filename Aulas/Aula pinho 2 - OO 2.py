class fruta: 

    def __init__(self, nome):
        self.nome = nome

    def envelhecer_na_despensa(self): 
        print(f"{self.nome} está envelhecendo na despensa enquanto você pede Ifood.")


banana = fruta("banana")
banana.envelhecer_na_despensa()
#raiz
fruta.envelhecer_na_despensa(banana)
print("#"*40)

maca = fruta("maca")
print(maca.__dict__)
print(vars(maca))

#mesmo que executar init 
maca.peso = 1 
maca.validade = "31/12/2025"



