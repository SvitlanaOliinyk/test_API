class TestClass:
    @classmethod
    def setup_class(cls):
        print('\nsetup_module()')

    @classmethod
    def teardown_class(module):
        print('\nteardown_module()')


    def setup_function(function):
        print('\nsetup_module()', function)


    def teardown_function(function):
        print('\nteardown_module()', function)


    def test_1():
        print('- test_1()')

    def test_2():
        print('- test_2()')