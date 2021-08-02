import os

from flask import Flask
from math import sqrt

app = Flask(__name__)

@app.route('/')
def hello_world():
    x = 0.0
    for j in range(1, 1_000_000):
        x += sqrt(j)
    return 'Sum of sqrt(x), x between 1 and 1 million is {}!\n'.format(x)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
