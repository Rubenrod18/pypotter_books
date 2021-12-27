import functools
import time


def seed_actions(fnc):
    @functools.wraps(fnc)
    def message(*args, **kwargs):
        seeder = args[0]

        print(' Seeding: %s' % seeder.name)
        exec_time = 0
        try:
            start = time.time()
            res = fnc(*args, **kwargs)
            exec_time = round((time.time() - start), 2)
        finally:
            print(' Seeded: {} ( {} seconds )'.format(seeder.name, exec_time))
        return res

    return message
