
class parent:
    def function1(self):
        print("This is function 1")

class child(parent):
    def function2(self,a):
        print("child class function 2")
        print(a)
b = 20
y = child()
y.function1()
y.function2(10)
print(y,b)