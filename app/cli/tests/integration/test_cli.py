import shutil

from flask import current_app

from app.blueprints.base import BaseCliTest


class TestCli(BaseCliTest):
    def setUp(self):
        super(TestCli, self).setUp()

    def test_is_cli_seeder_ok_execute_all_seeders_process_executed_successfully(  # noqa
        self,
    ):
        result = self.runner.invoke(args=['seed'])

        stdout_str = result.stdout_bytes.decode('utf-8')
        finished_message = 'Database seeding completed successfully'
        is_finished_process = stdout_str.find(finished_message) != -1

        self.assertEqual(0, result.exit_code)
        self.assertEqual(True, is_finished_process)

    def test_is_cli_component_cli_ok_run_cli_process_executed_successfully(
        self,
    ):
        with self.app.app_context():
            component_name = 'test_component_name'
            result = self.runner.invoke(
                args=['component', '--name', component_name]
            )

            self.assertEqual(0, result.exit_code)

            bp_path = current_app.config['BLUEPRINTS_DIRECTORY']
            component_abs_path = f'{bp_path}/{component_name}'
            shutil.rmtree(component_abs_path)

    def xtest_is_cli_flask_shell_ok(self):
        result = self.runner.invoke(args=['make', 'shell'])

        from pprint import pprint

        pprint(result.__dict__)

        self.assertEqual(0, result.exit_code)
