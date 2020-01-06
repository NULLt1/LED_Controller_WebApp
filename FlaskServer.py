from flask import Flask, render_template
import WS2801_Controller

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/power/')
def power():
    print("power")
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
