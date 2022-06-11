class Sun:
    instance = None

    @classmethod
    def inst(cls):
        if cls.instance is None:
            cls.instance = cls.__new__(cls)
        return cls.instance


def main():
    first = Sun.inst()
    second = Sun.inst()
    print(first is second)
    print(id(first))
    print(id(second))


if __name__ == "__main__":
    main()
