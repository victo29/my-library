from flask import Flask
from flask_login import LoginManager
from models.conection import get_db  # Presumindo que você tenha esta função
from controllers.UsuarioController import usuario_bp
from models.usuario import Usuario
# from controllers.PublicacaoController import publicacao_bp

app = Flask(__name__)
app.register_blueprint(usuario_bp)
# app.register_blueprint(publicacao_bp)

login_manager = LoginManager()
login_manager.init_app(app)

# Define a rota de login
login_manager.login_view = 'usuario_bp.logar'


@login_manager.user_loader
def load_user(user_id):
    # Aqui você deve carregar o usuário do banco de dados
    with get_db() as session:  # Use a função de obter a sessão que você definiu
        return session.query(Usuario).filter_by(id=user_id).first()


if __name__ == "__main__":

    app.secret_key = 'bb5d3680c0d90478ba469ff4a12b09b59df7525cd54b2e1235ddcd85bf2a5047' 
    app.run(debug=True)