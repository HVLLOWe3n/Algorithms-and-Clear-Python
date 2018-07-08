class Man:
    def __init__(self):
        self.__age = None        # private variables
        self.__name = None      # private variables

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return str(self.__age ) + ' and ' + self.__name


roman = Man()        # Object Class

roman.set_age(20)
roman.set_name('Roman')

print(roman, id(roman))
