class bank():
    balance=0
    accno=702568048
    pin=7025
    acctype='savings'
    name='Midhun'
    
    def __init__(self):
        self.accno=7025680485
        self.acctype='savings'
        self.balance=0

    def deposit(self):
        print("Hello ",self.name)
        deposit=int(input("Enter the amount to be deposited :- "))
        self.balance=self.balance+deposit
        print("Your available balance is:- ",self.balance,"rupees\n")

    def withdraw(self):
        print("Hello ",self.name)
        withdraw=int(input("Enter the amount to be withdrawn :- "))
        if(self.balance>withdraw):
                self.balance=self.balance-withdraw
                print("Your available balance is:- ",self.balance,"rupees\n")
        else:
             print("Insufficient balance :- ",self.balance,"rupees\n")
                     
    def balanc(self):
        print("Hello ",self.name)
        print("Your available balance is:- ",self.balance,"rupees\n")

b=bank()
name="Midhun"
pin=7025    
print("Hello sir")
n=int(input("Enter your pin:- "))
while(True):

    if n!=pin:
            print("Enter the correct pin\n")
            print("Please remove your card")
            exit(0)

    else:
            print("Hello",name)
            print("1.Deposit\n2.withdraw\n3.Balance\n4.Exit\n")
            ch=int(input("Enter your choice :- "))
            if ch==1:
                b.deposit()
            elif ch==2:
                b.withdraw()
            elif ch==3:
                b.balanc()
            elif ch==4:
                print("Thank you for your service have a good day")
                exit(0)
            else:
                print("Invalid Option")
    

    
        






































        
