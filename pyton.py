def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            print(f"{i} * {j} = {result}")

if __name__ == "__main__":
    multiplication_table()
