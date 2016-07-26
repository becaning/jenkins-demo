# encoding: utf-8

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    print("hello")
    return '<h1>hello world</h1>'


@app.route('/hello/<name>')
def hello(name):
    return '<h1>hello {}</h1>'.format(name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
