from ._base_integration_test import _BookBaseIntegrationTest


class TestGetBook(_BookBaseIntegrationTest):
    def test_is_book_obtained_book_exists_returns_book(self):
        with self.app.app_context():
            book = self.get_rand_book()

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.get(
                f'{self.base_path}/{book.id}', json={}, headers=auth_header
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(book.id, json_data.get('id'))
            self.assertEqual(book.title, json_data.get('title'))
            self.assertEqual(book.author, json_data.get('author'))
            self.assertEqual(book.description, json_data.get('description'))
            self.assertEqual(book.isbn, json_data.get('isbn'))
            self.assertEqual(book.total_pages, json_data.get('total_pages'))
            self.assertEqual(book.publisher, json_data.get('publisher'))
            self.assertEqual(
                book.published_date.strftime('%Y-%m-%d'),
                json_data.get('published_date'),
            )
            self.assertEqual(book.language, json_data.get('language'))
            self.assertEqual(book.dimensions, json_data.get('dimensions'))
            self.assertEqual(
                book.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('created_at'),
            )
            self.assertEqual(
                book.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('updated_at'),
            )
            self.assertEqual(book.deleted_at, json_data.get('deleted_at'))
