from app.blueprints.base import BaseTest
from app.decorators import seed_actions
from app.utils.disable_prints import DisablePrints


class _SeedExample:
    name = 'SeedExample'
    priority = -1

    @seed_actions
    def __init__(self):
        self.name = 'SeedExampleChanged'
        self.priority = 0


class TestSeedActions(BaseTest):
    """
    is_login_ok: is the unit of work.
    user_does_not_exist: is the scenario.
    returns_false: is the expected end result or behavior of the system.
    """

    def setUp(self):
        super(TestSeedActions, self).setUp()

    def test_is_seed_actions_ok_create_valid_seeder_seeder_executed_correctly(
        self,
    ):
        with DisablePrints():
            seed_example = _SeedExample()

        self.assertEqual(seed_example.name, 'SeedExampleChanged')
        self.assertEqual(seed_example.priority, 0)
