from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from models.usuario import Usuario


import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('register.html')
    
    # POST
    name = request.form.get('name')
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not name or not email or not pwd:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    try:
        novo_usuario = Usuario(email=email, password=pwd, name=name)
        novo_usuario.register()  
    except Exception as error:
        return jsonify({"error": str(error)}), 400

    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201

@usuario_bp.route('/', methods=['GET', 'POST'])
@usuario_bp.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'GET':
        return render_template('login.html')

    # POST
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email or not pwd:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    try:
        usuario_logado = Usuario(email=email, password=pwd)
        user = usuario_logado.login() 
        login_user(user) 
        return jsonify({"redirect": url_for('usuario_bp.get_home')})  
    except Exception as error:
        return jsonify({"error": str(error)}), 400
    
@usuario_bp.route('/home', methods=['GET'])
@login_required  
def get_home():
    return render_template('home.html', nome=current_user.name)


@usuario_bp.route('/logout', methods=['POST'])
@login_required  
def logout():
    logout_user()  
    return redirect(url_for('usuario_bp.get_logar'))