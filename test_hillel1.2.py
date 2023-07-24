# Тести
def test_generate_random_string():
    # Перевірка, що повертає строку правильної довжини (20 + 5 = 25)
    assert len(generate_random_string()) == 25

    # Перевірка, що повертає строку правильної довжини при іншій вказаній довжині (10 + 5 = 15)
    assert len(generate_random_string(10)) == 15

    # Перевірка, що повертає різні результати для різних викликів
    assert generate_random_string() != generate_random_string()

    # Перевірка, що останні 5 символів в результаті є довільною частиною (порівняємо з "ABCDE")
    assert generate_random_string()[-5:] != "ABCDE"

    print("Усі тести пройдено")

test_generate_random_string()`