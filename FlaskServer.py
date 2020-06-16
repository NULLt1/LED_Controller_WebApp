from flask import Flask, render_template, redirect, request
import WS2801Controller

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/power/')
def power():
    print("POWER")
    WS2801Controller.WS2801Controller.power()
    return redirect('/')

@app.route('/color/', methods=['POST'])
def color():
    print(int(request.values.get('red')),)
    print(int(request.values.get('green')),)
    print(int(request.values.get('blue')),)
    WS2801Controller.WS2801Controller.changeColor(color=(int(request.values.get('red')), int(request.values.get('green')), int(request.values.get('blue'))))
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
