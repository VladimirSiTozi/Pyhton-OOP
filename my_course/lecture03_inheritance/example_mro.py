class A:
    def hello(self):
        return 'hello from a'

class B:
    def hello(self):
        return 'hello from b'

class C:
    def hello(self):
        return 'hello from c'

class D(A, B, C):
    pass

d = D()
print(d.hello())
