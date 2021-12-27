import math
from collections import Counter
from typing import Union

from app.helpers import ListHelper
from app.helpers import StrHelper


class _CalBookPriceService:
    @staticmethod
    def calculate(books):
        """Calculate final price based on all collections.

        Parameters
        ----------
        books : list
            Book collections calculated. For example::

                [[0, 1, 3, 4], [0, 1, 3, 4], [0, 3], [3]]

        Returns
        -------
        float or int
            Calculated price.

        """
        book_price = 8
        books_final_price = 0

        for item in books:
            discount = 1
            total_units = len(item)

            if total_units == 5:
                discount = 0.75
            if total_units == 4:
                discount = 0.8
            if total_units == 3:
                discount = 0.9
            if total_units == 2:
                discount = 0.95

            books_final_price += book_price * total_units * discount

        return books_final_price

    @staticmethod
    def duplicates(needle, books):
        """

        Parameters
        ----------
        needle : list
            Values to search in the `books` param.
        books : list
            Contains the book id's.

        Returns
        -------
        list
            Book collections calculated.

        Example
        -------
        >>> needle = [0, 1, 3, 4]
        >>> lst = [0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 4]
        >>> _CalBookPriceService.duplicates(needle, lst)
        [[0, 1, 3, 4], [0, 1, 3, 4], [0, 3], [3]]

        """
        book_collections = []

        for item in needle:
            total_duplicated = StrHelper.total_count(item, books)

            for index in range(total_duplicated):
                try:
                    book_collections[index].append(item)
                except IndexError:
                    book_collections.append([item])

        return book_collections

    @staticmethod
    def check_four_discount_collections(
        books, books_collections, unique_books
    ):
        """Check four discount collections.

        If any collection has more than 4 items then one of them is added
        to the collection with minimum items.

        Parameters
        ----------
        books : list
            Contains the book id's.
        books_collections : list
            Contains the book collections calculated.
        unique_books : set
            Unique book id's.

        Returns
        -------
        list
            New book collections calculated.

        Example
        -------
        >>> books = [0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 4]
        >>> books_collections = [[0, 1, 3, 4], [0, 1, 3, 4], [0, 3], [3, 2]]
        >>> unique_books = {0, 1, 2, 3, 4}
        >>> _CalBookPriceService.check_four_discount_collections(
        >>>     books, books_collections, unique_books
        >>> )
        [[0, 1, 3], [0, 1, 3], [0, 3, 4], [3, 2, 4]]

        """
        if len(unique_books) == 5 and len(books) > 6:
            is_invalid = True
            while is_invalid:
                four_collections = math.floor(len(books) / 4)
                max_coll = 0
                for item in books_collections:
                    if len(item) >= 4:
                        max_coll += 1

                if four_collections != max_coll and max_coll > 0:
                    # TODO: improve this code for getting the min row
                    min_index = None
                    min_elements = len(books)
                    for index, item2 in enumerate(books_collections):
                        if len(item2) < min_elements:
                            min_elements = len(item2)
                            min_index = index

                    # TODO: improve this code for getting the max row
                    max_index = None
                    max_elements = -1
                    for index, item2 in enumerate(books_collections):
                        if len(item2) > max_elements:
                            max_elements = len(item2)
                            max_index = index

                    value = books_collections[max_index].pop(-1)
                    books_collections[min_index].append(value)
                else:
                    is_invalid = False

        return books_collections

    def cal_duplicate_book_collections(
        self, books: list, books_duplicated: list, unique_books: set
    ) -> list:
        """Calcuation duplicate book collections.

        Parameters
        ----------
        books : list
            Contains the book id's.
        books_duplicated : list
            Contains the book id's that has duplicated values in `books` param.
        unique_books : set
            Unique book id's.

        Returns
        -------
        list
            Book collections calculated. For example::

                [[0, 1, 2, 3, 4], [1]]
                [[0, 1], [0, 1]]

        """
        books_collections = self.duplicates(books_duplicated, books)
        c = Counter(books)
        common = [
            item for item in c.most_common() if item[0] not in books_duplicated
        ]

        for item in common:
            book_id, units = item[0], item[1]
            if len(unique_books) == 5 and len(books) > 6:
                min_index = None
                min_elements = len(books)
                for index, item2 in enumerate(books_collections):
                    if len(item2) < min_elements:
                        min_elements = len(item2)
                        min_index = index
                books_collections[min_index].append(book_id)
            elif units == 1:
                books_collections[0].append(book_id)

        books_collections = self.check_four_discount_collections(
            books, books_collections, unique_books
        )

        return books_collections

    def cal_collections(self, books: list) -> list:
        """Calculation book collections.

        The books are ordered by a collection with secuence number.
        The duplicated ID's are added to diferents collections.

        Parameters
        ----------
        books : list
            Contains the book id's. For example::

                [0, 1, 1, 2, 3, 4]

        Returns
        -------
        list
            Returns the books group by collection of five. For example::

                [[0, 1, 2, 3, 4], [1]]

        """
        books_collections = []

        if books:
            books.sort()
            unique_books = set(books)
            has_only_book = len(unique_books) == 1
            duplicated_books = ListHelper.duplicates(books)

            if has_only_book:
                books_collections = [[item] for item in books]
            elif not duplicated_books:
                books_collections = [books]
            else:
                books_collections = self.cal_duplicate_book_collections(
                    books, duplicated_books, unique_books
                )

        return books_collections

    def price(self, books: list) -> Union[float, int]:
        """Calculation books price.

        Parameters
        ----------
        books : list
            Contains the book id's. For example::

                [0, 1, 1, 2, 3, 4]

        Returns
        -------
        float or int
            Calculated price for books.

        """
        books_collections = self.cal_collections(books)
        return self.calculate(books_collections)
