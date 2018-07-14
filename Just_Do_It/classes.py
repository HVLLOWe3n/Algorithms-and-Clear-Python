class A:
    def __init__(self):
        pass

    def go(self):
        print('Go, A!')


class B(A):
    def __init__(self):
        super(B, self).__init__()

    def go(self, name):
        print('Go, {}'.format(name))
