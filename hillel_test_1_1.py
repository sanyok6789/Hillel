some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]

def is_valid_number(x):
    return isinstance(x, (int, float)) and x > 500

valid_data = list(filter(is_valid_number, some_data))

print(valid_data)  # Output: [501, 600]