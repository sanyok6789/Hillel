def is_valid_password(password):
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.islower() for char in password) or not any(char.isupper() for char in password):
        return False

    special_characters = "+-/*!\"№;%:?*()="
    if not any(char in special_characters for char in password):
        return False

    if " " in password:
        return False

    if not password.isascii():
        return False

    return True