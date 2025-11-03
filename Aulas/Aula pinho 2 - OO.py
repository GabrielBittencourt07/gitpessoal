class cachorro: 
    """
    Classe que representa um cachorro.
    """

    contador_cachorros = 0

    def __init__(self, nome, raca, idade):
        """lindo"""
        self.nome = nome
        self.raca = raca
        self.idade = idade 
        cachorro.contador_cachorros += 1

    def latido(self): 
        return "Au Au"
    
    @classmethod
    def get_numero_cachorros(cls): 
        return cls.contador_cachorros
    
    @classmethod
    def from_string(cls, string_cachorro): 
        nome, raca, idade = string_cachorro.split(",")
        return cls(nome, raca, idade)
    

cachorro_1 = cachorro("lulu", "buldog", 99)
cachorro_2 = cachorro("lala", "labrador", 25)
cachorro_3 = cachorro.from_string("Jade, golden, 0")

print(cachorro_1.latido())
print(cachorro.get_numero_cachorros())
print(cachorro.contador_cachorros)
        
        
        