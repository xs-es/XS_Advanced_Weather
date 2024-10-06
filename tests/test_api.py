# test_api.py
import unittest
from api.run_api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test the home route of the API"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Advanced Weather Application API", response.data)

    def test_get_weather_data(self):
        """Test the GET endpoint for weather data"""
        response = self.app.get('/api/v1/weather')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
