# test_main.py
import unittest
from main import main

class TestWeatherApp(unittest.TestCase):
    def test_main(self):
        """Test the main entry point of the weather app."""
        try:
            main()
        except Exception as e:
            self.fail(f"Main application failed with error: {e}")

if __name__ == '__main__':
    unittest.main()
