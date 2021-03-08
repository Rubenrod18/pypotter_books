from .manager import Role, RoleManager
from .serializers import role_serializer, roles_serializer
from .swagger import (role_input_sw_model, role_sw_model,
                      role_search_output_sw_model)
from .tests.factory import RoleFactory
