from flask import Flask, render_template
import WS2801Controller

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/power/')
def power():
    WS2801Controller.WS2801Controller.console_test()
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
