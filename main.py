from flask import Flask, render_template
from random import choice

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    random_name = choice(['Name_A', 'Name_B', 'Name_C'])
    return render_template('index.html', title = "Про Flask", name = random_name)

@app.route('/about')
def about():
    return render_template('about.html', title = "О сайте", nums = [i for i in range(5)])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)