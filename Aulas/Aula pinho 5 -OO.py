from abc import ABC, abstractmethod

class Account(ABC):  #Não da pra criar um abjeto da classe abstrata. Exemplo (2D e 3D seriam classes que definem a forma, mas não da pra criar um objeto "2D", mas da pra criar um objeto "quadrado" que herdaria as propriedades do pai 2D)
    @abstractmethod
    def deposit(self, amount: float): ... 

    @abstractmethod
    def withraw(self, amount: float): ...

    @abstractmethod 
    def apply_interest(self, amount: float): ...

    @abstractmethod 
    def charge_fee(self, amount: float): ...

    #Essa classe é uma bosta (segundo o Pinho)


class SavingAccount(Account): 

    def deposit(self, amount: float): 
        print(f"depositando {amount}")

    def withraw(self, amount: float):
        print(f"sacando {amount}")

    def apply_interest(self, amount: float): 
        print(f"Aplicando juros")


class ChekingAccount(Account): 

    def deposit(self, amount: float): 
        print(f"depositando {amount}")

    def withraw(self, amount: float):
        print(f"sacando {amount}")

    def apply_interest(self, amount: float): #Fiz um atibuto que rende alguma coisa em uma classe que não deveria render nada (algo esta errado)
        print(f"Nada a fazer")

    def charge_fee(self, amount: float):
        print(f"Cobrando a taxa mensal")




acc1 = SavingAccount()
print(acc1)