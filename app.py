from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bem-vindo à minha aplicação Flask!</h1><p>Esta é a página inicial.</p>"

@app.route('/sobre')
def sobre():
    return "<h1>Sobre</h1><p>Este é um site de exemplo feito com Flask.</p>"

if __name__ == '__main__':
    app.run(debug=True)
