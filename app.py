from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bem-vindo à minha aplicação Flask!</h1><p>augusto daora</p>"

@app.route('/sobre')
def sobre():
    return "<h1>Sobre</h1><p>augusto daora</p>"

if __name__ == '__main__':
    app.run(debug=True)
