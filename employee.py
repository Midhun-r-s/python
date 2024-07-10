class person:
    def __init__(self):
        self.name=input('Enter the name:')
        self.code=int(input('Enter the code'))
    def display(self):
        print("name is ",self.name)
        print("code is ",self.code)
class account(person):
    def __init__(self):
        self.pay=int(input('Enter the payment:'))
    
    def display(self):
        super().__init__()
        super().display()
        print("payment is ",self.pay)
class admin(account):
    def __init__(self):
        self.exp=int(input('Enter the experience year:'))
    def display(self):
        super().__init__()
        super().display()
        print("experience is ",self.exp)
class employee(admin):
    pass

a=employee()
a.display()
