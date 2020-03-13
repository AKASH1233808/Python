#python program to overload equality
#and less than operator

class A:
    def ___init__(self,a):
        self.a = a

    def __it__(self,other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
        
