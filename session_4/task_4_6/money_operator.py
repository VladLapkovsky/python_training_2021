from functools import total_ordering


class Initializer:
    exchange_rate = {
        "EUR": 0.93,
        "BYN": 2.1,
        "USD": 1,
        "JPY": 110.86,
    }

    def __init__(self, amount_of_money, currency="USD"):
        self.amount_of_money = amount_of_money
        self.currency = currency
        self.rate = self.exchange_rate.get(currency)
        self.amount_in_default_currency = self.amount_of_money / self.rate


@total_ordering
class Comparisons(Initializer):
    def __eq__(self, other):
        return self.amount_in_default_currency == other.amount_in_default_currency

    def __lt__(self, other):
        return self.amount_in_default_currency < other.amount_in_default_currency


class Operations(Initializer):
    def __repr__(self):
        return self.amount_of_money

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                round(self.amount_of_money + other, 2),
                self.currency,
            )
        return self.__class__(
            round((self.amount_in_default_currency + other.amount_in_default_currency) * self.rate, 2),
            self.currency,
        )

    __radd__ = __add__

    def __neg__(self):
        return -self.amount_of_money

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return (self - self * 2) + other

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                round(self.amount_of_money * other, 2),
                self.currency,
            )
        return self.__class__(
            round((self.amount_in_default_currency * other.amount_in_default_currency) * self.rate, 2),
            self.currency,
        )

    __rmul__ = __mul__

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                round(self.amount_of_money // other, 2),
                self.currency,
            )
        return self.__class__(
            round((self.amount_in_default_currency // other.amount_in_default_currency) * self.rate, 2),
            self.currency,
        )

    def __rfloordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                round(other // self.amount_of_money, 2),
                self.currency,
            )
        return self.__class__(
            round((other.amount_in_default_currency // self.amount_in_default_currency) * self.rate, 2),
            self.currency,
        )

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                round(self.amount_of_money / other, 2),
                self.currency,
            )
        return self.__class__(
            round((self.amount_in_default_currency / other.amount_in_default_currency) * self.rate, 2),
            self.currency,
        )

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                round(other / self.amount_of_money, 2),
                self.currency,
            )
        return self.__class__(
            round((other.amount_in_default_currency / self.amount_in_default_currency) * self.rate, 2),
            self.currency,
        )


class Money(Comparisons, Operations):
    def __str__(self):
        return f"{self.amount_of_money} {self.currency}"


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8)
    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)
