import textwrap


class Pagination:
    def __init__(self, input_text, symbol_on_page):
        self.input_text = input_text
        self.symbol_on_page = symbol_on_page
        self.wrapped_list = textwrap.wrap(
            self.input_text, self.symbol_on_page, drop_whitespace=False,
        )

    def __getattr__(self, attr):
        if attr == "item_count":
            return len(self.input_text)
        if attr == "page_count":
            return len(self.wrapped_list)
        raise TypeError("Wrong attr")

    def count_items_on_page(self, page):
        try:
            return len(self.wrapped_list[page])
        except Exception:
            raise IndexError("Invalid index. Page is missing.")

    def find_page(self, symbols):
        querying_pages = []
        for elem in self.wrapped_list:
            if elem.strip() in symbols or symbols in elem:
                querying_pages.append(self.wrapped_list.index(elem))
        if querying_pages:
            return querying_pages
        raise ValueError(f"{symbols} is missing on the pages")

    def display_page(self, page):
        try:
            return self.wrapped_list[page]
        except Exception:
            raise IndexError("Invalid index. Page is missing.")


def main():
    pages = Pagination("Your beautiful text", 5)
    print(pages.wrapped_list)
    print(pages.page_count)  # 4
    print(pages.item_count)  # 19

    print()

    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))

    print()

    try:
        print(pages.count_items_on_page(4))
    except Exception as exp:
        print(exp)

    print()

    print(pages.find_page("Your"))
    print(pages.find_page("e"))
    print(pages.find_page("beautiful"))
    print(pages.find_page(" "))

    print()

    try:
        print(pages.find_page("great"))
    except Exception as exp:
        print(exp)

    print()

    print(pages.display_page(0))


if __name__ == "__main__":
    main()
