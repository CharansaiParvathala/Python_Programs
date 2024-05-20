class Outer():
    def __init__(self):
        print('Outer Object is created')
        self.inner = self.Inner()
    class Inner():
        def __init__(self):
            print('Inner class Object created')
obj = Outer()