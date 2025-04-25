import peoples
import accounts

class AuthenticationFailureError(Exception): ...
#BANCO 
class Bank:
    def __init__(
            self,
            agencies: list[int] | None =  None,
            clients: list[peoples.Client] | None = None,
            accounts: list[accounts.Account] | None = None):
        
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def authentication(self, account, client):

        def _account_client_check() -> bool:
            if client.account is not account:
                raise AuthenticationFailureError('You account not is from client.')
            
            return True

        def _agencies_check() -> bool:
            if account.agency in self.agencies:
                return True
            
            return False
        
        def _client_check() -> bool:
            if client in self.clients:
                return True
            
            return False
        
        def _account_check() -> bool:
            if client.account in self.accounts:
                return True
            
            return False
        
        if _agencies_check() and _account_check() and _client_check() and _account_client_check():
            return True
        
        raise AuthenticationFailureError('Sorry, but your account doesn\'t is in our bank.')
    
    def __repr__(self) -> str:
        attrs = f'({self.agencies!r}), ({self.clients!r}), ({self.accounts!r}))'
        return f'{type(self).__name__}: {attrs}'
