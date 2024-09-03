from models.conection  import connection
from models.publicacao import Publicacao
import uuid
import os
class PublicacaoService:

    
    def _salvar_arquivo(self, file) -> str:
        novo_nome = str(uuid.uuid4())
        ext_file = os.path.splitext(file.filename)[1].lower()
        path = "data/" + novo_nome + ext_file
        file.save("../" + path)
        
        return path

    def inserir(self, publicacao : Publicacao) -> bool | Exception:

        
        nome_livro = publicacao.nome_livro
        quantidade_paginas =  publicacao.quantidade_paginas
        resenha = publicacao.resenha
        avaliacao = publicacao.avaliacao
        id_usuario = publicacao.id_usuario
        
        try:
            path = self._salvar_arquivo(publicacao.file)
            
            conn = connection()
            cursor = conn.cursor()

            insert_query = "INSERT INTO publicacao (path_foto_capa ,nome_livro , resenha_livro, avaliacao, qtd_paginas, id_usuario) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_query,(path, nome_livro, resenha, avaliacao, quantidade_paginas, id_usuario))
            conn.commit()
            cursor.close()
            conn.close

            return True
        except:
            raise Exception ("Erro ao salvar publicação")

        

        
