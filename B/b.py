class bankaccount :
    def __init__(self,accname,initialammount):
        self.name = accname
        self.balance = initialammount
        print(f"\nAccount {self.name} is created with balance = ${self.balance}")

