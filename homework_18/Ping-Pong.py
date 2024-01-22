from flask import Flask, abort, request

app = Flask(__name__)


@app.route('/')
@app.route('/ping')
def ping_page():
    return (f'<html><head><title></title></head>'
            f'<body><h1></h1>'
            f'<ul><a href="/pong">ping</a></ul>'
            f'</body>'
            f'</html>')


@app.route('/pong')
def pong_page():
    return (f'<html><head><title></title></head>'
            f'<body><h1></h1>'
            f'<ul><a href="/ping">pong</a></ul>'
            f'</body>'
            f'</html>')

if __name__ == '__main__':
    app.run(port=8080, debug=True)