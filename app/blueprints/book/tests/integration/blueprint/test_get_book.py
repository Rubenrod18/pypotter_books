from ._base_integration_test import _BookBaseIntegrationTest


class TestGetBook(_BookBaseIntegrationTest):
    def test_is_book_obtained_book_exists_returns_book(self):
        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.get(
            f'{self.base_path}/{self.book.id}', json={}, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.book.id, json_data.get('id'))
        self.assertEqual(self.book.title, json_data.get('title'))
        self.assertEqual(self.book.author, json_data.get('author'))
        self.assertEqual(self.book.description, json_data.get('description'))
        self.assertEqual(self.book.isbn, json_data.get('isbn'))
        self.assertEqual(self.book.total_pages, json_data.get('total_pages'))
        self.assertEqual(self.book.publisher, json_data.get('publisher'))
        self.assertEqual(
            self.book.published_date.strftime('%Y-%m-%d'),
            json_data.get('published_date'),
        )
        self.assertEqual(self.book.language, json_data.get('language'))
        self.assertEqual(self.book.dimensions, json_data.get('dimensions'))
        self.assertEqual(
            self.book.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('created_at'),
        )
        self.assertEqual(
            self.book.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('updated_at'),
        )
        self.assertEqual(self.book.deleted_at, json_data.get('deleted_at'))
        self.assertEqual(
            f'{self.base_path}/{self.book.id}',
            json_data.get('_links', {}).get('self'),
        )
        self.assertEqual(
            f'{self.base_path}/search',
            json_data.get('_links', {}).get('collection'),
        )
