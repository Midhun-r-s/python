class rectangle1:
    
    def area1(self):
        print(" --------First Rectangle--------\n")
        print("............Area............")
        l1=int(input("Enter the lenght of first rectangle :- "))
        b1=int(input("Enter the breadth of first rectangle :- "))
        area1=l1*b1
        print("The area is :- ",area1)
        return area1
   
    def area2(self):
        print(" \n--------Second Rectangle--------\n")
        print("............Area............")
        l2=int(input("Enter the lenght of second rectangle :- "))
        b2=int(input("Enter the breadth of second rectangle :- "))
        area2=l2*b2
        print("The area is :- ",area2)
        return area2
        

rec1=rectangle1()
a1=rec1.area1()

a2=rec1.area2()

if a1>a2:
    print("\nThe area of  first rectangle  is larger")
else:
     print("\nThe area of  second rectangle  is larger")
