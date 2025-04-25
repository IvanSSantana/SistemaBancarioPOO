from abc import ABC, abstractmethod

#CONTAS
class Account(ABC):
    def __init__(self, agency: int, id: int):
        self.agency = agency
        self.id = id
        self.balance: float = 0
        
    @abstractmethod
    def withdraw(self, value: float) -> float: ... #Polimorfismo nas sub-classes

    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'Deposit: {value}')
        return self.balance

    def details(self, msg=''):
        print(f'Your balance is R${self.balance:.2f}. {msg}')

    def __repr__(self) -> str:
        attrs = f'({self.agency!r}), ({self.id!r}), ({self.balance!r})'
        return f'{type(self).__name__}: {attrs}'    

class LimitError(Exception): ...
class SavingAccount(Account):
    def withdraw(self, value):
        if value > self.balance:
            raise LimitError(f'Sorry. Denied withdraw in R${value}.')

        self.balance -= value
        self.details(f'Withdraw: {value}')
        return self.balance

class CheckingAccount(Account):
    def __init__(self, agency, id, limit = 0):
        super().__init__(agency, id) 
        self.limit = limit #Limite extra das conta-correntes

    def withdraw(self, value):
        if value > (self.balance + self.limit):
            raise LimitError(f'Sorry. Invalid value for withdraw. Your limit: {self.limit}.')
        
        self.balance -= value
        self.details(f'Withdraw: {value}')
        return self.balance
    
    def __repr__(self) -> str:
        attrs = f'({self.agency!r}), ({self.id!r}), ({self.balance!r}), ({self.limit!r})'
        return f'{type(self).__name__}: {attrs}'
