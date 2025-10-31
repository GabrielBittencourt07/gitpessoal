"""aprendendo Orinetação Objeto"""
from datetime import datetime 

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
    def __init__(self, owner: str, currency: str = "BRL",  initial_balance: float = 0.0):
        """lindo"""
        self.customer = owner
        self.currency = currency
        self._balance = float(initial_balance)
        self.created_at = datetime.now().isoformat(timespec="seconds")
        self.__str__ = f"Account of {owner}"

        if hasattr(self.customer, "add_account"): 
            self.customer.add_account(self)
        
        print(f"[INFO] Account created for {self.customer} in {self.created_at}")
    
    
    
    def deposit(self, amount: (float, int)) -> None: 
        """lindo"""
        if amount <= 0: 
            raise NegativeAmountError("[ERROR] Withdrawal must be positive.")
        self._balance += amount
        print(f"[OK] Deposited {amount: .2f} {self.currency}. New balance {self._balance: .2f}")
    
    
    
    def withdraw(self, amount: (float, int)) -> None: 
        """lindo"""
        if amount <= 0: 
            raise NegativeAmountError("[ERROR] Withdrawal must be positive.")
        if amount > self._balance:
            raise InsuficientFoundsError("[ERROR] Insufficient fund.")
        self._balance -= amount

        return self.balance
    
    @property
    def balance(self): 
        return self._balance

    @balance.setter
    def balance(self, new_balance: float) -> float:
        if new_balance != new_balance :
            raise BankingError("[ERROR] Balance cannot be set to NoN.")
        self._balance = float(new_balance)
    
    def __str__(self) -> str: 
        return f"Account (owner = {self.customer}), currency = {self.currency}, balance = {self.balance}"



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