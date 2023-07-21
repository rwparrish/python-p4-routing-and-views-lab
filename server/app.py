#!/usr/bin/env python
import ipdb
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    count = f''
    for num in range(parameter):
        count += f'{num}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # ipdb.set_trace()
    if operation == '+':
        value = num1 + num2
        return f'{value}'
    elif operation == '-':
        value = num1 - num2
        return f'{value}'
    elif operation == 'div':
        value = num1 / num2
        return f'{value}'
    elif operation == '*':
        value = num1 * num2
        return f'{value}'
    elif operation == '%':
        value = num1 % num2
        return f'{value}'
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
