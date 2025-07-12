from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def gallery():
    return render_template('gallery.html')

@app.route('/carta')
def letter():
    return render_template('letter.html')

if __name__ == '__main__':
    app.run(debug=True) 