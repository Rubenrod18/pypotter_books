import unittest

from app.blueprints.book.services.book_price_service import BookPriceService


class TestBookPriceService(unittest.TestCase):
    def setUp(self):
        self.book_price_service = BookPriceService()

    def test_is_book_price_ok_basic_discounts_returns_calculated_price(self):
        self.assertEqual(0, self.book_price_service.price([]))
        self.assertEqual(8, self.book_price_service.price([1]))
        self.assertEqual(8, self.book_price_service.price([2]))
        self.assertEqual(8, self.book_price_service.price([3]))
        self.assertEqual(8, self.book_price_service.price([4]))
        self.assertEqual(8 * 3, self.book_price_service.price([1, 1, 1]))

    def test_is_book_price_ok_simple_discounts_returns_calculated_price(self):
        self.assertEqual(8 * 2 * 0.95, self.book_price_service.price([0, 1]))
        self.assertEqual(8 * 3 * 0.9, self.book_price_service.price([0, 2, 4]))
        self.assertEqual(
            8 * 4 * 0.8, self.book_price_service.price([0, 1, 2, 4])
        )
        self.assertEqual(
            8 * 5 * 0.75, self.book_price_service.price([0, 1, 2, 3, 4])
        )

    def test_is_book_price_ok_several_discounts_returns_calculated_price(self):
        self.assertEqual(
            8 + (8 * 2 * 0.95), self.book_price_service.price([0, 0, 1])
        )
        self.assertEqual(
            2 * (8 * 2 * 0.95), self.book_price_service.price([0, 0, 1, 1])
        )
        self.assertEqual(
            (8 * 4 * 0.8) + (8 * 2 * 0.95),
            self.book_price_service.price([0, 0, 1, 2, 2, 3]),
        )
        self.assertEqual(
            8 + (8 * 5 * 0.75),
            self.book_price_service.price([0, 1, 1, 2, 3, 4]),
        )

    def test_is_book_price_ok_edge_cases_returns_calculated_price(self):
        self.assertEqual(
            2 * (8 * 4 * 0.8),
            self.book_price_service.price([0, 0, 1, 1, 2, 2, 3, 4]),
        )
        self.assertEqual(
            3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8),
            self.book_price_service.price(
                [
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    1,
                    1,
                    1,
                    1,
                    2,
                    2,
                    2,
                    2,
                    3,
                    3,
                    3,
                    3,
                    3,
                    4,
                    4,
                    4,
                    4,
                ]
            ),
        )
