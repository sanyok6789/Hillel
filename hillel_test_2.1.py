import unittest

class TestPasswordValidation(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(is_valid_password("Pa$$w0rd"))
        self.assertTrue(is_valid_password("H3ll0+World"))
        self.assertTrue(is_valid_password("P@ssw0rd!"))

    def test_invalid_password(self):
        self.assertFalse(is_valid_password("Abc123"))
        self.assertFalse(is_valid_password("Short12"))
        self.assertFalse(is_valid_password("Привіт123"))
        self.assertFalse(is_valid_password("NoDigits!"))
        self.assertFalse(is_valid_password("Spaces Are Bad"))

if __name__ == "__main__":
    unittest.main()
