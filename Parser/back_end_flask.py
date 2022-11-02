from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "Це головна сторінка"


@app.route('/hello')
def hello_world():
    return "Привіт, світе"


@app.route('/hello/<name>')
def hello_name(name: str):
    return f"Привіт, {name}"


if __name__ == '__main__':
    app.run()
