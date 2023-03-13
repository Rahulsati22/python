# hybrid inheritance is the combination of multiple inheritance and single inheritance
class Base:
    pass


class Derived1(Base):
    pass


class Derived2(Base):
    pass


class Derived3(Derived1, Derived2):
    pass
