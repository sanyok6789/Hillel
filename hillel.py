from secrets import token_urlsafe

def generate_random_string(length=20):
    random_string = token_urlsafe(length)
    additional_part = "ABCDE"  # Ваша довільна частина довжиною 5 символів
    return random_string + additional_part


