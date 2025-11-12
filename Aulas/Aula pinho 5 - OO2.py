"""aprendendo Orinetação Objeto"""
from datetime import datetime 
from __future__ import annotations

#classe são receitas que ensinam o python a criar um objeto 

class BankingError(Exception): pass
class NegativeAmountError(BankingError): pass
class InsuficientFoundsError(BankingError): pass


class account :
    """
    Representa uma conta bancárias simples. 
    
    Atributos: 
            Owner (str) : None of the account holder
            currency(str): Acount currency code (e.g, "BRL", "USD").
            balance (float): Current balance of the account.
            
    Methods: 
            deposit(amount): ...
            withdraw(amount): ...
            show_balance(): ...

    Examples: 
        ...
    """
    def __init__(self, owner: customer, currency: str = "BRL",  initial_balance: float = 0.0):
        """lindo"""
        self._customer = owner
        self._currency = currency
        self._balance = float(initial_balance)
        self._created_at = datetime.now().isoformat(timespec="seconds")
        self._customer.add_account(self)

    prop
    def balance(self) -> float: 
        return self._balance 
    
    def deposit(self,  amount : float ) -> float: 
        self._balance += amount 
    
    def withdraw(self, amount: float) -> float: 
        self._balance -= amount

    def monthly_update(self) -> None: 
        print(f"A classe {self.__class__.__name__} não precisa de atualizações mensais")
    




class customer: 
    """lindo"""
    def __init__(self, name: str, email: str):
        self.name = name
        self.email =email 
        self._account = list[account] = []
        pass

    def add_account(self, account: account): 
        if account not in self.accounts:
            self._account.append(account)
        pass
    
    @property
    def accounts(self) -> list[account]:
        return list[self.account] 
        

#Falta encapsular o resto das aplicações que usamos {self._balance} para usar-mos {self.get_balance} 
#Driver Code
acc1 = account("gabriel", "BRL", 20)

acc1.deposit(1000)
acc1.withdraw(1015)
acc1._balance += 10
print(acc1)