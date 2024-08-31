from flask import Flask
from controllers.UsuarioController import usuario_bp
from controllers.PublicacaoController import publicacao_bp

app = Flask(__name__)

#  chave -> sha256


app = Flask(__name__, template_folder='views')
app.register_blueprint(usuario_bp)
app.register_blueprint(publicacao_bp)


if __name__ == "__main__":
    app.secret_key = 'bb5d3680c0d90478ba469ff4a12b09b59df7525cd54b2e1235ddcd85bf2a5047' 
    app.run(debug=True)