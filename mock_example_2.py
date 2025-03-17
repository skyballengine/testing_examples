from unittest.mock import Mock

mock = Mock()

# Make multiple calls with first method
mock.func("Hello World")
mock.func("Greetings Planet")

# Make second method call
mock.other_func("Hola")

# Print first method call count
print('func call count: {}\n'.format(mock.func.call_count))

# Print last args called on first method
print('func last args: {}\n'.format(mock.func.call_args))

# Print all the args called on first method
print('func args list: {}\n'.format(mock.func.call_args_list))

# Print all the methods called on our Mock object
print('all methods called: {}'.format(mock.method_calls))
