from flask import Flask, render_template,redirect
import WS2801Controller

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/power/')
def power():
    print("power")
    WS2801Controller.WS2801Controller.power()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
