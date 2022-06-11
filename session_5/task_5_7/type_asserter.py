class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if hasattr(value, "__iter__"):
            for elem in value:
                self._type_error(elem)
        else:
            self._type_error(value)
        instance.__dict__[self.name] = value

    def _type_error(self, value_to_check):
        if not isinstance(value_to_check, self.expected_type):
            raise TypeError("MyNumberCollection supports only numbers!")

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def type_assert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate
