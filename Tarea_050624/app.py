from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')
        
        if operation == 'sum':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2

    return render_template('index.html', name="Tu Nombre", group="Tu Grupo", result=result)

if __name__ == '__main__':
    app.run(debug=True)
