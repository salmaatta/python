class a :
    def do_something(self) :
        print ("From class a")

class b (a):
    def do_something(self) :
        print ("From class b")
    

my_instance = b()
my_instance.do_something()    