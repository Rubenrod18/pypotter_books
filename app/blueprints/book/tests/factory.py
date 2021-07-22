import base64
import os
import random

import factory

from app.blueprints.book import Book
from app.extensions import db

_CURRENT_PATH = '%s/../' % os.path.dirname(os.path.abspath(__file__))


def _get_base64_image(book_path: str = None):
    with open(book_path, 'rb') as fd:
        base64_image = base64.b64encode(fd.read())
    return base64_image


class BookFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Book
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    # Normal fields
    title = factory.Faker('sentence')
    author = factory.Faker('name_nonbinary')
    description = factory.Faker('text')
    isbn = factory.Faker('isbn13')
    total_pages = random.randint(100, 500)
    publisher = factory.Faker('name_nonbinary')
    published_date = factory.Faker('date')
    language = factory.Faker('language_name')

    @factory.lazy_attribute
    def dimensions(self):
        height = round(random.uniform(10, 13), 1)
        width = round(random.uniform(1, 3), 1)
        length = round(random.uniform(15, 20), 1)

        return f'{length} x {width} x {height} cm'

    @factory.lazy_attribute
    def image(self):
        book_image_path = (
            f'{_CURRENT_PATH}/images/hp_{random.randint(1, 5)}.jpg'
        )
        return random.choice([None, _get_base64_image(book_image_path)])


class HarryPotterPartOneBookFactory(BookFactory):
    title = 'Harry Potter and the philosopher\'s stone'
    author = 'J.K. Rowling'
    description = 'Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry\'s eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure is about to begin! These new editions of the classic and internationally bestselling, multi-award-winning series feature instantly pick-up-able new jackets by Jonny Duddle, with huge child appeal, to bring Harry Potter to the next generation of readers. It\'s time to PASS THE MAGIC ON.'  # noqa
    isbn = '978-1408855652'
    total_pages = 352
    publisher = 'Bloomsbury'
    published_date = '2014-08-01'
    language = 'English'
    dimensions = '12.9 x 2.3 x 19.7 cm'
    image = _get_base64_image(f'{_CURRENT_PATH}/images/hp_1.jpg')


class HarryPotterPartTwoBookFactory(BookFactory):
    title = 'Harry Potter and the chamber of secrets'
    author = 'J.K. Rowling'
    description = 'Harry Potter\'s summer has included the worst birthday ever, doomy warnings from a house-elf called Dobby, and rescue from the Dursleys by his friend Ron Weasley in a magical flying car! Back at Hogwarts School of Witchcraft and Wizardry for his second year, Harry hears strange whispers echo through empty corridors - and then the attacks start. Students are found as though turned to stone ...Dobby\'s sinister predictions seem to be coming true. These new editions of the classic and internationally bestselling, multi-award-winning series feature instantly pick-up-able new jackets by Jonny Duddle, with huge child appeal, to bring Harry Potter to the next generation of readers. It\'s time to PASS THE MAGIC ON.'  # noqa
    isbn = '978-1408855669'
    total_pages = 384
    publisher = 'Bloomsbury'
    published_date = '2014-09-01'
    language = 'English'
    dimensions = '13.1 x 2.4 x 19.8 cm'
    image = _get_base64_image(f'{_CURRENT_PATH}/images/hp_2.jpg')


class HarryPotterPartThreeBookFactory(BookFactory):
    title = 'Harry Potter and the prisoner of Azkaban'
    author = 'J.K. Rowling'
    description = 'When the Knight Bus crashes through the darkness and screeches to a halt in front of him, it\'s the start of another far from ordinary year at Hogwarts for Harry Potter. Sirius Black, escaped mass-murderer and follower of Lord Voldemort, is on the run - and they say he is coming after Harry. In his first ever Divination class, Professor Trelawney sees an omen of death in Harry\'s tea leaves ...But perhaps most terrifying of all are the Dementors patrolling the school grounds, with their soul-sucking kiss. These new editions of the classic and internationally bestselling, multi-award-winning series feature instantly pick-up-able new jackets by Jonny Duddle, with huge child appeal, to bring Harry Potter to the next generation of readers. It\'s time to PASS THE MAGIC ON.'  # noqa
    isbn = '978-1408855676'
    total_pages = 480
    publisher = 'Bloomsbury'
    published_date = '2014-08-01'
    language = 'English'
    dimensions = '13 x 3.1 x 19.7 cm'
    image = _get_base64_image(f'{_CURRENT_PATH}/images/hp_3.jpg')


class HarryPotterPartFourBookFactory(BookFactory):
    title = 'Harry Potter and the globet of fire'
    author = 'J.K. Rowling'
    description = 'The Triwizard Tournament is to be held at Hogwarts. Only wizards who are over seventeen are allowed to enter - but that doesn\'t stop Harry dreaming that he will win the competition. Then at Hallowe\'en, when the Goblet of Fire makes its selection, Harry is amazed to find his name is one of those that the magical cup picks out. He will face death-defying tasks, dragons and Dark wizards, but with the help of his best friends, Ron and Hermione, he might just make it through - alive! These new editions of the classic and internationally bestselling, multi-award-winning series feature instantly pick-up-able new jackets by Jonny Duddle, with huge child appeal, to bring Harry Potter to the next generation of readers. It\'s time to PASS THE MAGIC ON.'  # noqa
    isbn = '978-1408855683'
    total_pages = 640
    publisher = 'Bloomsbury'
    published_date = '2014-08-01'
    language = 'English'
    dimensions = '12.9 x 4.1 x 19.8 cm'
    image = _get_base64_image(f'{_CURRENT_PATH}/images/hp_4.jpg')


class HarryPotterPartFiveBookFactory(BookFactory):
    title = 'Harry Potter and the order the phoenix'
    author = 'J.K. Rowling'
    description = 'Dark times have come to Hogwarts. After the Dementors\' attack on his cousin Dudley, Harry Potter knows that Voldemort will stop at nothing to find him. There are many who deny the Dark Lord\'s return, but Harry is not alone: a secret order gathers at Grimmauld Place to fight against the Dark forces. Harry must allow Professor Snape to teach him how to protect himself from Voldemort\'s savage assaults on his mind. But they are growing stronger by the day and Harry is running out of time. These new editions of the classic and internationally bestselling, multi-award-winning series feature instantly pick-up-able new jackets by Jonny Duddle, with huge child appeal, to bring Harry Potter to the next generation of readers. It\'s time to PASS THE MAGIC ON.'  # noqa
    isbn = '978-1408855690'
    total_pages = 815
    publisher = 'Bloomsbury'
    published_date = '2014-08-01'
    language = 'English'
    dimensions = '13 x 5.2 x 19.8 cm'
    image = _get_base64_image(f'{_CURRENT_PATH}/images/hp_5.jpg')
