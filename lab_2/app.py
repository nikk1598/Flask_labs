from flask import Flask, render_template


MESSAGE_TO_SHOW = 'Hello, World!!!'

app = Flask(__name__)


@app.route('/')
def show():
    return render_template('show.html', message=MESSAGE_TO_SHOW)


if __name__ == '__main__':
    app.run(port=8080)
