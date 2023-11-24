import pytest


@pytest.fixture
def person():
    return 'John'


@pytest.fixture
def end_of_story():
    yield
    print('The end')


@pytest.fixture(scope='class', autouse=True)
def big_end_of_story():
    yield
    print('The end of story')
