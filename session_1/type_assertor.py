import functools
import inspect


def type_assert(*ty_args, **ty_kwargs):
    def decorate(func):
        sig = inspect.signature(func)
        bound_types = sig.bind(*ty_args, **ty_kwargs).arguments

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, input_value in bound_values.arguments.items():
                if name in bound_types:
                    value_type = bound_types.get(name)
                    if not isinstance(input_value, value_type):
                        raise TypeError(f"Argument {name} must be {value_type}")
            return func(*args, **kwargs)

        return wrapper

    return decorate
