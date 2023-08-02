import unittest

class TestRandomNumberGeneration(unittest.TestCase):
    def test_random_number(self):
        for _ in range(1000):
            random_number = generate_random_number()
            self.assertGreaterEqual(random_number, 0)
            self.assertLessEqual(random_number, 1000)

if __name__ == "__main__":
    unittest.main()



