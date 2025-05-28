from flask import Flask, jsonify, request
import traceback

app = Flask(__name__)

# Custom exception classes
class RateLimitExceeded(Exception):
    """Exception raised when rate limit is exceeded."""
    pass

class ThrottleExceeded(Exception):
    """Exception raised when throttle limit is exceeded."""
    pass

class InvalidRequestException(Exception):
    """Exception raised when the request is invalid."""
    pass

# Error handlers
@app.errorhandler(RateLimitExceeded)
def handle_rate_limit_error(error):
    return jsonify(Error="Rate limit exceeded", 
                  Message=str(error)), 429

@app.errorhandler(ThrottleExceeded)
def handle_throttle_error(error):
    return jsonify(Error="Throttle limit exceeded", 
                  Message=str(error)), 429

@app.errorhandler(InvalidRequestException)
def handle_invalid_request(error):
    return jsonify(Error="Invalid request", 
                  Message=str(error)), 400

@app.errorhandler(Exception)
def handle_generic_error(error):
    app.logger.error(f"Unexpected error: {error}")
    app.logger.error(traceback.format_exc())
    return jsonify(Error="Internal server error", 
                  Message="An unexpected error occurred"), 500

@app.route('/rate-limit-me')
def rateLimit():
    try:
        # Implement rate limiting logic here
        # For demo purposes, we'll just return success
        return jsonify(Result="Rate-Limit-Success"), 200
    except Exception as e:
        # Specific exceptions will be caught by the error handlers
        raise

@app.route('/throttle-me')
def throttle():
    try:
        # Implement throttling logic here
        # For demo purposes, we'll just return success
        return jsonify(Result="Throttle-Limit-Success"), 200
    except Exception as e:
        # Specific exceptions will be caught by the error handlers
        raise

# Test routes for exception handling
@app.route('/test/rate-limit-error')
def test_rate_limit_error():
    raise RateLimitExceeded("You have exceeded the rate limit")

@app.route('/test/throttle-error')
def test_throttle_error():
    raise ThrottleExceeded("You have exceeded the throttle limit")

@app.route('/test/invalid-request')
def test_invalid_request():
    raise InvalidRequestException("Invalid parameter in request")

@app.route('/test/generic-error')
def test_generic_error():
    raise Exception("Something went wrong")

if __name__ == "__main__":
    app.run(debug=True, port=7000)
