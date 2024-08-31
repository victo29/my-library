from werkzeug.datastructures import FileStorage
from models.conection  import connection
import bleach
import os


class Publicacao:

    def __init__(self, nome_livro: str, resenha: str, avaliacao: int, file: FileStorage, id_usuario: int, quantidade_paginas: int, ) -> None:
        self.nome_livro = nome_livro
        self.resenha = resenha
        self.avaliacao = avaliacao
        self.file = file
        self.quantidade_paginas = quantidade_paginas
        self.id_usuario = id_usuario

    @property
    def nome_livro(self):
        return self._nome_livro
    
    @property
    def quantidade_paginas(self):
        return self._quantidade_paginas
    
    @property
    def resenha(self):
        return self._resenha
    
    @property
    def file(self):
        return self._file   
    
    @property
    def avaliacao(self):
        return self._avaliacao
    
    @property
    def id_usuario(self):
        return self._id_usuario


    @nome_livro.setter
    def nome_livro(self, nome):
        self._nome_livro = bleach.clean(nome)

    @quantidade_paginas.setter
    def quantidade_paginas(self, valor):
        self._quantidade_paginas = valor
    
    @resenha.setter
    def resenha(self, text):
        self._resenha = bleach.clean(text)

    @avaliacao.setter
    def avaliacao(self, valor):
        self._avaliacao = valor
    
    @id_usuario.setter
    def id_usuario(self,id):
       self._id_usuario = id

    @file.setter
    def file(self, file):

        if not self._verifica_extensao(file):
            raise Exception ("A extensão do arquivo não é permitida")
        if not self._verifica_tamanho(file):
            raise Exception ("O tamanho do arquivo não é permitido, max 10MB")

        self._file = file

    def _verifica_tamanho(self, file: FileStorage):
        max_tamanho = 10485760
        tamanho_file = file.content_length

        return tamanho_file <= max_tamanho
    
    def _verifica_extensao(self, file: FileStorage):
        extensoes_permitidas = ['.jpg', '.png', '.jpeg']

        filename = file.filename
        extensao_arquivo = os.path.splitext(filename)[1]

        return extensao_arquivo.lower() in extensoes_permitidas


