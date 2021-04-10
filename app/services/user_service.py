import logging

from marshmallow import EXCLUDE

from app.blueprints.role import RoleManager
from app.blueprints.user import UserManager, user_serializer
from app.blueprints.user.models import user_datastore
from app.extensions import db
from app.services.base_service import BaseService

logger = logging.getLogger(__name__)


class UserService(BaseService):

    def __init__(self, *args, **kwargs):
        super(UserService, self).__init__(*args, **kwargs)
        self.manager = UserManager()
        self.role_manager = RoleManager()
        self.user_serializer = user_serializer

    def create(self, user_data):
        deserialized_data = self.user_serializer.load(user_data)

        try:
            role = self.role_manager.find(deserialized_data['role_id'])
            deserialized_data.pop('role_id')

            user = self.manager.get_last_record()
            fs_uniquifier = 1 if user is None else user.id + 1

            # FIXME: comment next line when auth is enabled
            # deserialized_data.update({'created_by': current_user.id,
            deserialized_data.update({'created_by': None,
                                      'roles': [role],
                                      'fs_uniquifier': fs_uniquifier})
            user = user_datastore.create_user(**deserialized_data)
            db.session.commit()
        except Exception as e:
            logger.debug(e)
            db.session.rollback()
            raise

        return user

    def find(self, user_id: int, *args):
        self.user_serializer.load({'id': user_id}, partial=True)
        return self.manager.find(user_id, *args)

    def save(self, user_id: int, **kwargs):
        kwargs['id'] = user_id
        deserialized_data = self.user_serializer.load(kwargs, unknown=EXCLUDE)

        user = self.manager.find(user_id)
        try:
            if 'role_id' in deserialized_data:
                user_datastore.remove_role_from_user(user, user.roles[0])
                role = self.role_manager.find(deserialized_data['role_id'])
                user_datastore.add_role_to_user(user, role)
                deserialized_data.pop('role_id')

            self.manager.save(user_id, **deserialized_data)
            db.session.commit()
        except Exception as e:
            logger.debug(e)
            db.session.rollback()
            raise

        db.session.refresh(user)
        return user

    def delete(self, user_id: int):
        self.user_serializer.load({'id': user_id}, partial=True)
        user = self.manager.delete(user_id)
        db.session.commit()
        return user
