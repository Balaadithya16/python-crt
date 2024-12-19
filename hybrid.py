class school:
    def display(self):
        print("This is school")
class s1(school):
    def s1fun(self):
        print("S1 function")
class s2(s1,school):
    def s2fun(self):
        print("S2 function")
o=s2()
o.display()
o.s1fun()
    
    