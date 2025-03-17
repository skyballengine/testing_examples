from unittest.mock import Mock

# Creat Mock object
mock = Mock()

# Print unassigned mock attribute
print(mock.attr)

# Assign mock attribute and print
mock.attr = "Hello World"
print(mock.attr)

# Call unassigned mock method
print(mock.func())

# Assign mock method and call
mock.func = print
mock.func(mock.attr)

# Set return_value
mock.abs.return_value = "7"

print(mock.abs(-7))

mock.abs.assert_called()
mock.abs.assert_called_once()
mock.abs.assert_called_with(-7)
mock.abs.assert_called_once_with(-7)
print(mock.abs.call_count)
print(mock.abs.call_args)
