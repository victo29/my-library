from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from models.usuario import Usuario


import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    pwd = data.get('password')

    if not name or not email or not pwd:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    try:
        novo_usuario = Usuario(email=email, password=pwd, name=name)
        novo_usuario.register()  
    except Exception as error:
        return jsonify({"error": str(error)}), 400

    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201



@usuario_bp.route('/logar', methods=['POST'])
def logar():

    data = request.get_json()

    email = data.get('email')
    pwd = data.get('password')

    if not email or not pwd:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    try:
        usuario_logado = Usuario(email=email, password=pwd)
        user = usuario_logado.login() 
        login_user(user) 
        return jsonify({"userData": current_user.name}), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 400
    

@usuario_bp.route('/home', methods=['GET'])
@login_required  
def get_home():
    return "" # Em construção


@usuario_bp.route('/logout', methods=['POST'])
@login_required  
def logout():
    logout_user()  
    return "" # Em construção