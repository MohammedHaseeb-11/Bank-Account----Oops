class balanceexception(Exception) :
    pass
class bankaccount :
    def __init__(self,accname,initialammount):
        self.name = accname
        self.balance = initialammount
        print(f"\nAccount {self.name} is created \nBalance = &{self.balance:.2f}")


    def getbalance(self):
        print(f"\nAccount '{self.name}' Balance = '&{self.balance:.2f}'")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getbalance()

    def viabletransaction(self,amount):
        if self.balance >= amount:
            return
        else :
            raise balanceexception(
                f"\nSorry, account'{self.name}' has only balance '{self.balance:.2f}"
            )
    def withdraw(self,amount):
        try :
            self.viabletransaction(amount)
            self.balance= self.balance - amount
            print("\n withdraw complete")
            self.getbalance()
        except balanceexception as error:
            print(f"\nWithdraw interrupted : '{error}'")

    def transfer(self,amount,account):
        try :
            self.viabletransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
        except balanceexception as error :
            print(f"\nTransfer intrerupted , {error}")


