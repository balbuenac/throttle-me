import unittest
from app import app, RateLimitExceeded, ThrottleExceeded, InvalidRequestException

class TestExceptionManagement(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def test_rate_limit_endpoint_success(self):
        response = self.app.get('/rate-limit-me')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['Result'], 'Rate-Limit-Success')
    
    def test_throttle_endpoint_success(self):
        response = self.app.get('/throttle-me')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['Result'], 'Throttle-Limit-Success')
    
    def test_rate_limit_exceeded(self):
        response = self.app.get('/test/rate-limit-error')
        data = response.get_json()
        self.assertEqual(response.status_code, 429)
        self.assertEqual(data['Error'], 'Rate limit exceeded')
        self.assertEqual(data['Message'], 'You have exceeded the rate limit')
    
    def test_throttle_exceeded(self):
        response = self.app.get('/test/throttle-error')
        data = response.get_json()
        self.assertEqual(response.status_code, 429)
        self.assertEqual(data['Error'], 'Throttle limit exceeded')
        self.assertEqual(data['Message'], 'You have exceeded the throttle limit')
    
    def test_invalid_request(self):
        response = self.app.get('/test/invalid-request')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['Error'], 'Invalid request')
        self.assertEqual(data['Message'], 'Invalid parameter in request')
    
    def test_generic_exception(self):
        response = self.app.get('/test/generic-error')
        data = response.get_json()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['Error'], 'Internal server error')

if __name__ == '__main__':
    unittest.main()