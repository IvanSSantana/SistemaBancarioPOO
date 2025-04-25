import peoples, accounts
from bank import Bank

if __name__ == '__main__':
    client_ivan = peoples.Client('Ivan', 18)
    client_ivan.account = accounts.CheckingAccount(111, 1)
    client_nino = peoples.Client('Nino', 14)
    client_nino.account = accounts.SavingAccount(222, 2)

    bank = Bank()

    bank.clients += client_nino, client_ivan
    bank.accounts += client_nino.account, client_ivan.account
    bank.agencies += client_nino.account.agency, client_ivan.account.agency

    client_mae = peoples.Client('Valquiria', 10000)
    client_mae.account = accounts.SavingAccount(333, 3)

    if bank.authentication(client_ivan.account, client_ivan):
        client_ivan.account.deposit(100.50)