class Greeter(object):
    #Constructor
    def __init__(self, name):
        self.myName = name
        
    def sayHiTo(self, name, short=True):
        if short:
            print('Hello, %s!' % name)
        else:
            print('Hello, %s, I\'m %s!' % (name, self.myName)) #This line uses a Tuple data type
        
g = Greeter('Foo')
g.sayHiTo('Bar')
g.sayHiTo('Bar', short=False)
