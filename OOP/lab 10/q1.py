class A:
    def __init__(self):
        print("A's Construcotr")

    def printInfo(self):
        print("A's Method")

class B(A):
    def __init__(self):
        print("B's Constructor")
        super().__init__()
    
    def printInfo(self):
        print("B's Method")
    
class C(A):
    def __init__(self):
        print("C's Constructor")
        super().__init__()

    def printInfo(self):
        print("C's Method")

class D(B, C):
    def __init__(self):
        print("D's Constructors")
        super().__init__()

obj = D()


# obj1 = B()
# obj2 = A()
# obj = C()

#obj.printInfo()


