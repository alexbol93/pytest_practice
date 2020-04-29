import pytest
import random
import string


@pytest.fixture()
def random_string():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


@pytest.fixture()
def random_number():
    return random.randint(0, 123)
