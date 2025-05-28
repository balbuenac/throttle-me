from locust import HttpUser, task, between

class ThrottleUser(HttpUser):
    """
    Locust user class that simulates users accessing the rate limiting and throttling endpoints.
    
    This user will wait between 1 and 5 seconds between each task execution.
    """
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds between tasks
    
    @task
    def rate_limit_endpoint(self):
        """
        Task to test the rate-limit-me endpoint.
        Verifies that the response contains the expected result and status code.
        """
        with self.client.get("/rate-limit-me", catch_response=True) as response:
            if response.status_code == 200:
                if "Rate-Limit-Success" in response.text:
                    response.success()
                else:
                    response.failure("Response did not contain 'Rate-Limit-Success'")
            else:
                response.failure(f"Got status code {response.status_code}")
    
    @task
    def throttle_endpoint(self):
        """
        Task to test the throttle-me endpoint.
        Verifies that the response contains the expected result and status code.
        """
        with self.client.get("/throttle-me", catch_response=True) as response:
            if response.status_code == 200:
                if "Throttle-Limit-Success" in response.text:
                    response.success()
                else:
                    response.failure("Response did not contain 'Throttle-Limit-Success'")
            else:
                response.failure(f"Got status code {response.status_code}")

"""
To run this locust script:

1. Start the Flask application in a separate terminal:
   $ python app.py

2. Start the Locust server:
   $ locust

3. Open your browser and navigate to http://localhost:8089/
   - Enter the number of users to simulate
   - Enter the spawn rate (users spawned per second)
   - Set the host to http://localhost:7000
   - Click "Start swarming"

4. Alternatively, run it from the command line:
   $ locust --host=http://localhost:7000 --users=20 --spawn-rate=5 --run-time=30s --headless
"""