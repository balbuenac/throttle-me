from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/rate-limit-me')
def rateLimit():
    return jsonify(Result="Rate-Limit-Success"), 200

@app.route('/throttle-me')
def throttle():
    return jsonify(Result="Throttle-Limit-Success"), 200

if __name__ == "__main__":
    app.run(debug=True, port=7000)
