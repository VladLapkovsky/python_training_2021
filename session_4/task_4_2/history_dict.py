"""This module provides one class to increment incoming values.

Class:
    HistoryDict
"""


class HistoryDict:
    """Class that create dictionary that will memorize n latest changed keys (n=10 by default).

    Create history for each instance separately.
    """

    def __init__(self, custom_dict, dict_len=10):
        """Accept the input dict and the latest_changed_keys_len.

        Parameters:
            custom_dict: HistoryDict({"key": value})
            dict_len: max len of the keys_changes list
        """
        self.custom_dict = custom_dict
        self.dict_len = dict_len
        self.changed_keys = []

    def set_value(self, new_key, new_value):
        """Adding new pair dict[key] = value .

        Parameters:
            new_key: new dict key.
            new_value: new dict values.
        """
        self.custom_dict[new_key] = new_value
        self.changed_keys.append(new_key)
        if len(self.changed_keys) > self.dict_len:
            self.changed_keys.pop(0)

    def get_history(self):
        """Return list of last changed dict keys.

        Returns:
            List like ["key", "key"...].
        """
        return self.changed_keys


def main():
    """Test HistoryDict class."""
    one = HistoryDict({"foo": 42})
    one.set_value("bar", 43)
    print(one.get_history())
    one.set_value("var", 43)
    print(one.get_history())
    one.set_value("zar", 43)
    print(one.get_history())
    one.set_value("dar", 43)
    print(one.get_history())
    one.set_value("gar", 43)
    print(one.get_history())

    print("-" * 80)

    two = HistoryDict({"qwe": 42}, dict_len=2)
    two.set_value("asd", 43)
    print(two.get_history())
    two.set_value("zxc", 43)
    print(two.get_history())
    two.set_value("rty", 43)
    print(two.get_history())
    two.set_value("fgh", 43)
    print(two.get_history())
    two.set_value("vbn", 43)
    print(two.get_history())


if __name__ == "__main__":
    main()
