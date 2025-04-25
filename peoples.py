import accounts

#PESSOA
class Person:
    def __init__(self, name: str, age: int):
        self._name = name.capitalize()
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name.capitalize()
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self) -> str:
        attrs = f'({self.name!r}), ({self.age})'
        return f'{type(self).__name__}: {attrs}'

#CLIENTE
class Client(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account: accounts.Account | None = None

    def __repr__(self) -> str:
        attrs = f'({self.name!r}), ({self.age}), ({self.account})'
        return f'{type(self).__name__}: {attrs}'