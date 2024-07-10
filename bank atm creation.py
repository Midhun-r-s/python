class bank:
    def __init__(self):
        self.accno=7025680485
        self.name='Midhun'
        self.acctype='savings'
        self.pin=7025
        self.balance=0
    def deposit(self):
        pin=int(input("Enter your 4 digit Pin :- "))
        if pin==self.pin:
            print("Hello",self.name)
            deposit=int(input("Enter the amount to be deposited :- "))
            self.balance=self.balance+deposit
            print("The avilable balance is:- ",self.balance)
        else:
            print("Invalid pin Please Remove Your Card")
            
    def withdraw(self):
        pin=int(input("Enter your 4 digit Pin :- "))
        if pin==self.pin:
            print("Hello",self.name)
            withdraw=int(input("Enter the amount to be withdrawn:- "))
            if self.balance>withdraw:
                self.balance=self.balance-withdraw
                print("The available balance is:- ",self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid pin Please Remove Your Card")
            
    def balanc(self):
        print("Hello",self.name)
        print("Your Available Balance is:- ",self.balance)
       
print("Hello Sir")
b=bank()        
while(True):
    print("MENU")
    print("-------")
    print("1.DEPOSIT\n2.WITHDRAW\n3.BALANCE\n4.EXIT")
    n=int(input("Enter Your Choice :- "))
    if n==1:
        b.deposit()
    elif n==2:
        b.withdraw()
    elif n==3:
        b.balanc()
    elif n==4:
        print("Thank You")
        exit(0)
    else:
        print("Wrong Choice")
    
