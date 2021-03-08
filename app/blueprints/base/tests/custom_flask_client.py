import logging

from flask import Response
from flask.testing import FlaskClient

logger = logging.getLogger(__name__)


class CustomFlaskClient(FlaskClient):
    @staticmethod
    def __before_request(*args, **kwargs):
        logger.info(f'args: {args}')
        logger.info(f'kwargs: {kwargs}')

    @staticmethod
    def __log_request_data(response: Response):
        if response.mimetype == 'application/json':
            response_data = response.get_json()
        else:
            response_data = response.data
        logger.info(f'response data: {response_data}')

    def __after_request(self, response: Response):
        logger.info(f'response status code: {response.status_code}')
        logger.info(f'response mime type: {response.mimetype}')
        self.__log_request_data(response)

    def __make_request(self, method: str, *args, **kwargs):
        logger.info('< === START REQUEST === >')
        self.__before_request(*args, **kwargs)

        kwargs['method'] = method
        response = self.open(*args, **kwargs)

        self.__after_request(response)
        logger.info('< === END REQUEST === >')
        return response

    def get(self, *args, **kwargs):
        """Like open but method is enforced to GET."""
        return self.__make_request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        """Like open but method is enforced to POST."""
        return self.__make_request('POST', *args, **kwargs)

    def put(self, *args, **kwargs):
        """Like open but method is enforced to PUT."""
        return self.__make_request('PUT', *args, **kwargs)

    def delete(self, *args, **kwargs):
        """Like open but method is enforced to DELETE."""
        return self.__make_request('DELETE', *args, **kwargs)
