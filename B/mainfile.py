from b import bankaccount

haseeb = bankaccount("Mohammed_haseeb",100010)
haseeb2 = bankaccount("Mohammed_haseeb",150000)

haseeb.getbalance()
haseeb2.getbalance()

haseeb.deposit(100010)
haseeb2.deposit(15000)

haseeb.withdraw(100)

haseeb.transfer(100,haseeb2)