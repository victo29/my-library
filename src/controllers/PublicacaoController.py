import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from flask import Blueprint,  request, jsonify, redirect, url_for, session
from models.publicacao import Publicacao
from models.publicacaoService import PublicacaoService


publicacao_bp = Blueprint( 'publicacao_bp',__name__)
@publicacao_bp.route('/publicar-post', methods=['POST'])
def publicar():

   try:      
      nome_livro = request.form.get('nomeInput')
      avaliacao = request.form.get('radioInputs')
      resenha = request.form.get('resenhaInput')
      quantidade_paginas = request.form.get('qtdPagsInput')
      file = request.files['fileInput']
      id_usuario = session['usuario']['id']

      publicacao = Publicacao(nome_livro, resenha, avaliacao, file , id_usuario, quantidade_paginas)

      service = PublicacaoService()
      service.inserir(publicacao)

      return jsonify({"message": "Publicação realizada com sucesso!"}), 201
   except Exception as error:
      return jsonify({"error": error.args[0] }), 400