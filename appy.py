from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ropa')
def ropa():
    return render_template('ropa.html')

@app.route('/maquillaje')
def maquillaje():
    return render_template('maquillaje.html')

@app.route('/skincare')
def skincare():
    return render_template('skincare.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
