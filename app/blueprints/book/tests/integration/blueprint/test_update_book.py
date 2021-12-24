import factory

from ...factories import BookFactory
from ._base_integration_test import _BookBaseIntegrationTest
from app.helpers import DictHelper


class TestUpdateBook(_BookBaseIntegrationTest):
    def test_is_book_updated_book_exist_previously_returns_book(
        self,
    ):
        data = DictHelper.ignore_keys(
            factory.build(dict, FACTORY_CLASS=BookFactory),
            exclude=['image'],
        )

        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{self.book.id}',
            json=data,
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.book.id, json_data.get('id'))
        self.assertEqual(data['author'], json_data.get('author'))
        self.assertEqual(data['description'], json_data.get('description'))
        self.assertEqual(data['isbn'], json_data.get('isbn'))
        self.assertEqual(data['total_pages'], json_data.get('total_pages'))
        self.assertEqual(data['publisher'], json_data.get('publisher'))
        self.assertEqual(
            data['published_date'], json_data.get('published_date')
        )
        self.assertEqual(data['language'], json_data.get('language'))
        self.assertEqual(data['dimensions'], json_data.get('dimensions'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
        self.assertEqual(
            f'{self.base_path}/{self.book.id}',
            json_data.get('_links', {}).get('self'),
        )
        self.assertEqual(
            f'{self.base_path}/search',
            json_data.get('_links', {}).get('collection'),
        )
