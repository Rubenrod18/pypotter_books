import math
from collections import Counter

from app.helpers import ListHelper
from app.helpers import StrHelper


class BookPriceService:
    @staticmethod
    def calculate(books):
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
    def duplicates(needle, lst):
        book_collections = []

        for item in needle:
            total_duplicated = StrHelper.total_count(item, lst)

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
        if len(unique_books) == 5 and len(books) > 6:
            is_invalid = True
            while is_invalid:
                four_collections = math.floor(len(books) / 4)
                max_coll = 0
                for item in books_collections:
                    if len(item) >= 4:
                        max_coll += 1

                if four_collections != max_coll:
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
        self, books, books_duplicated, unique_books
    ):
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

    def cal_collections(self, books):
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

    def price(self, books):
        books_collections = self.cal_collections(books)
        return self.calculate(books_collections)
