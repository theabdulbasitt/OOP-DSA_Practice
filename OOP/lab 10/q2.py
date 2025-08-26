class A:
    def __init__(self):
        print("A's Constructor")

class B:
    def __init__(self):
        print("B's Constructor")
    
class C( B ,A):
    def __init__(self):
        super().__init__()  # calls according to MRO
        A.__init__(self)
        print("C's Constructor")

obj = C()
