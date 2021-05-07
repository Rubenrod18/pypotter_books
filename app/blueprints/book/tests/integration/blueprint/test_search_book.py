from ._base_integration_test import _BookBaseIntegrationTest


class TestSearchBooks(_BookBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_book_exist_book_title_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'title',
                        'field_value': book.title,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book.title, json_data.get('title'))

    def test_search_book_exist_book_author_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'author',
                        'field_value': book.author,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book.author, json_data.get('author'))

    def test_search_book_exist_book_description_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'description',
                        'field_value': book.description,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book.description, json_data.get('description'))

    def test_search_book_exist_book_isbn_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'isbn',
                        'field_value': book.isbn,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book.isbn, json_data.get('isbn'))

    def test_search_book_exist_book_total_pages_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'total_pages',
                        'field_value': book.total_pages,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book.total_pages, json_data.get('total_pages'))

    def test_search_book_exist_book_publisher_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'publisher',
                        'field_value': book.publisher,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book.publisher, json_data.get('publisher'))

    def test_search_book_exist_book_published_date_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'published_date',
                        'field_value': book.published_date.strftime(
                            '%Y-%m-%d'
                        ),
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(
                book.published_date.strftime('%Y-%m-%d'),
                json_data.get('published_date'),
            )

    def test_search_book_exist_book_language_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'language',
                        'field_value': book.language,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book.language, json_data.get('language'))

    def test_search_book_exist_book_dimensions_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()
            payload = {
                'search': [
                    {
                        'field_name': 'dimensions',
                        'field_value': book.dimensions,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book.dimensions, json_data.get('dimensions'))
