import pytest


@pytest.fixture(scope='session') # по умолчвнию scope='function'
def fixt1():
    print('\nInitialization of fixure')
    fixture = 'I am a fixture'
    yield fixture
    print('\nDestroying of fixure')


def test_1(fixt1):
    print('- test_1()')
    assert fixt1


def test_2(fixt1):
    print('- test_2()')
    assert 1 == 1


def test_3():
    print('- test_3()')
    assert 1 == 1
