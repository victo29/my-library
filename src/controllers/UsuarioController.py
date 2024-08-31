import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from models.usuario import Usuario



usuario_bp = Blueprint( 'usuario_bp',__name__)


@usuario_bp.route('/cadastrar', methods=['GET'])
def get_cadastrar():

    return render_template('cadastro.html')
    


@usuario_bp.route('/', methods=['GET'])
@usuario_bp.route('/logar', methods=['GET'])
def get_logar():
    return render_template('login.html')
    

@usuario_bp.route('/home', methods=['GET'])
def get_home():
    if 'logedin' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('usuario_bp.get_logar'), code=302)
    
@usuario_bp.route('/publicar', methods=['GET'])
def get_publicar():
    if 'logedin' in session:
        return render_template('publicar.html')
    else:
        return redirect(url_for('usuario_bp.get_logar'), code=302)


@usuario_bp.route('/get-dados-usuario', methods=['GET'])
def get_dados_usuario():
    return jsonify(session['usuario'])




@usuario_bp.route('/cadastrar-post', methods=['POST'])
def cadastrar():
    
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    if not nome or not email or not senha:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400  # Provavelmente não será necessário

    try:
        novo_usuario = Usuario(email,senha,nome)
        novo_usuario.cadastrar()
    except Exception as error:
        return jsonify({"error": error.args[0]}), 400
        

    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201


@usuario_bp.route('/logar-post', methods=['POST'])
def logar():

    email = request.form.get('email')
    senha = request.form.get('senha')

    if not email or not senha:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400 # Provavelmente não será necessário
    
    try:
        usuario_logado = Usuario(email,senha)
        usuario_logado.logar()
    except Exception as error:
        return jsonify({"error": error.args}), 400
    
    return jsonify({"redirect": url_for('usuario_bp.get_home')})