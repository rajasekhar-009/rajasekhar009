from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

# Sample function to simulate data traffic flow in the multi-cloud environment
@app.route('/simulate_traffic', methods=['GET'])
def simulate_traffic():
    # Simulate data flow between cloud environments
    cloud_traffic = {
        "cloud_1": random.randint(500, 1000),  # Random data amount in MB
        "cloud_2": random.randint(500, 1000)   # Random data amount in MB
    }
    
    # Simulate some processing time
    time.sleep(2)  # Simulate latency
    return jsonify(cloud_traffic)

if __name__ == '__main__':
    app.run(debug=True)
