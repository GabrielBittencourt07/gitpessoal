class Foo:
    def _init_(self):
        self.public # Atributo público - permite que o usuário altere a partir da instância/do objeto
        self._protected # Atributo protegido - não acontece "nada", apenas mostra que queremos proteger o objeto.
        # Na herança, "public" e "_protected" vão ser passados para as classes filho.
        self.__private # Atributo privado - cria uma camada de dificuldade, alertando ao usuário para não alterar desde a instâcia do objeto.
        # Não bloqueia alterações, apenas alerta e cria uma camada de dificuldade.
        # Apenas essa classe pode usar, classes filhas não recebem.

# Todos os métodos enxergam "private", haja vista que são da MESMA classe, não de classes filhas.
# Os outros ("public" e "protected") são enxergados normalmente, pois não tem restrição.
    def public_method(self):
        print("Olá, eu sou o método público")
        self._protected_method()
        self.__private_method()

    def _protected_method(self):
        print("Olá, eu sou o método protegido")
        self.__private_method()

    def __private_method(self):
        print("Olá, eu sou o método privado")
        

class Bar(Foo):
    pass

object_ = Foo()

print(object_.public_method())