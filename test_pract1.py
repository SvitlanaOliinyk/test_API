def setup_module(module):
    print('\nsetup_module()', module)


def teardown_module(module):
    print('\nteardown_module()', module)


def setup_function(function):
    print('\nsetup_module()', function)


def teardown_function(function):
    print('\nteardown_module()', function)


def test_1():
    print('- test_1()')

def test_2():
    print('- test_2()')