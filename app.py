from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='.')

# Simple rule-based responses
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "I'm still learning. Can you rephrase that?"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    response = get_response(user_message)
    return jsonify({'response': response})

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)