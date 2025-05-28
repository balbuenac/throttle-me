# Throttle Me

A simple Flask application with endpoints for testing rate limiting and throttling.

## Application Endpoints

- `/rate-limit-me`: Returns a JSON response with "Result": "Rate-Limit-Success"
- `/throttle-me`: Returns a JSON response with "Result": "Throttle-Limit-Success"

## Running the Application

```bash
# Install dependencies
pip install flask

# Run the Flask app
python app.py
```

The application will start on http://localhost:7000

## Load Testing

### Using JMeter

Run the existing JMeter test file:

```bash
jmeter -n -t RateThrottle.jmx -l results.jtl
```

### Using Locust

Locust is a modern load testing framework that allows you to define user behavior in Python code.

#### Installation

```bash
pip install locust
```

#### Running Locust with Web UI

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Start Locust:
   ```bash
   locust
   ```

3. Open your browser and go to http://localhost:8089/
   - Set the number of users to simulate
   - Set the spawn rate (users per second)
   - Enter the host: http://localhost:7000
   - Click "Start swarming"

#### Running Locust from Command Line

```bash
# Run with 20 users, spawning 5 users per second, for 30 seconds
locust --host=http://localhost:7000 --users=20 --spawn-rate=5 --run-time=30s --headless

# Export statistics to HTML report
locust --host=http://localhost:7000 --users=20 --spawn-rate=5 --run-time=30s --headless --html=report.html
```

#### Locust Test Configuration

The Locust test simulates users making requests to both endpoints:
- `/rate-limit-me`
- `/throttle-me`

Each simulated user waits between 1-5 seconds between requests to simulate real-world behavior.