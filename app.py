from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Your form page

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    email = request.form.get('email')  # Assuming the form has an input with name="email"
    
    # Process the data (Example: print it)
    print(f"Received email: {email}")
    
    # Example response
    return jsonify({"message": "Data received successfully", "email": email})

if __name__ == '__main__':
    app.run(debug=True)
