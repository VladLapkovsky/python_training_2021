class Bird:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} bird can walk and fly"

    def fly(self):
        print(f"{self.name} bird can fly")

    def walk(self):
        print(f"{self.name} bird can walk")


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        self.ration = ration
        super().__init__(name)

    def eat(self):
        print(f"It eats mostly {self.ration}")


class NonFlyingBird:
    def __init__(self, name, ration="fish"):
        self.name = name
        self.ration = ration

    def __str__(self):
        return f"{self.name} bird can walk and swim"

    def walk(self):
        print(f"{self.name} bird can walk")

    def eat(self):
        print(f"It eats mostly {self.ration}")

    def swim(self):
        print(f"{self.name} bird can swim")


class SuperBird(NonFlyingBird, FlyingBird):
    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


if __name__ == "__main__":
    b = Bird("Any")
    b.walk()
    b.fly()
    print(str(b))

    print()

    c = FlyingBird("Canary")
    c.walk()
    c.fly()
    c.eat()
    print(str(c))

    print()

    p = NonFlyingBird("Penguin")
    p.swim()
    p.walk()
    p.eat()
    try:
        p.fly()
    except AttributeError as exp:
        print(exp)
    print(str(p))

    print()

    s = SuperBird("Gull")
    s.walk()
    s.swim()
    s.fly()
    s.eat()
    print(str(s))
