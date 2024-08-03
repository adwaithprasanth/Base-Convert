from flask import Flask, render_template, request
from convert import convert_to_decimal, convert_from_decimal

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        from_base = int(request.form['from_base'])
        to_base = int(request.form['to_base'])

        decimal = convert_to_decimal(number, from_base)
        result = convert_from_decimal(decimal, to_base)

        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
