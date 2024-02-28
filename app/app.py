from flask import Flask



app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/health')
def health_check():
    # Add your custom health check logic here
    if all_required_services_are_running():
        return 'OK', 200
    else:
        return 'Service Unavailable', 500

# Example health check logic, replace it with your actual logic
def all_required_services_are_running():
    # Replace this with your logic to check the health of your services
    # For example, check if the required processes are running
    return True














if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)