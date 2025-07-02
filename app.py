from flask import Flask, render_template, request, jsonify
from convert import perform_conversion # Import the new function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    number = data.get('number')
    from_base = int(data.get('from_base'))
    to_base = int(data.get('to_base'))

    # Use the imported function
    result = perform_conversion(number, from_base, to_base)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)