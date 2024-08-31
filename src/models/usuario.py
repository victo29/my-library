from models.conection  import connection
from flask import session
from hashlib import sha256
import bleach
import re

class Usuario:

    def __init__(self, email: str, senha: str, nome:str = "Default",) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha



    # Getter
    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self._email
    
    @property
    def senha(self):
        return self._senha
    
    #Setter
    @nome.setter
    def nome(self, nome):
        self._nome = bleach.clean(nome) 

    @email.setter
    def email(self, email):
        self._email = bleach.clean(email)

    @senha.setter
    def senha(self, senha):

        hash_senha = sha256(senha.encode())
        self._senha = hash_senha.hexdigest()


    
    # PRIVATE MÉTODOS
    def _verifica_senha_fraca(self) -> bool:
    
        senha = self.senha
        numeros = re.findall(r'\d', senha)

        if len(senha) < 6 or len(numeros) < 2:
            return True
        
       
        return False




    def _verifica_nome_email (self) -> bool:
        conn = connection()
        cursor = conn.cursor()
        
        select_query = f"SELECT * FROM usuario where nome = %s OR email = %s"
        cursor.execute(select_query,(self.nome,self.email))
        
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            return False
        else:
            return True
    


    def _verifica_existencia_usuario(self):
        conn = connection()
        cursor = conn.cursor()

        select_query = "SELECT * FROM usuario WHERE email = %s"
        cursor.execute(select_query, (self.email,))  # Passando o e-mail como uma tupla


        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
      
            column_names = [desc[0] for desc in cursor.description]

            user = dict(zip(column_names, result))

            cursor.close()
            conn.close()

            return user
        else: 
            return False



    # PUBLIC MÉTODS

    def cadastrar(self):
  
        if(self._verifica_nome_email()):


            #ADICIONAR VERIFICAÇÃO DE SENHA


            conn = connection()
            cursor = conn.cursor()

            insert_query = f"INSERT INTO usuario (nome, email, senha) VALUES (%s,%s,%s)"
            cursor.execute(insert_query,(self.nome, self.email, self.senha))
            conn.commit()
            cursor.close()
            conn.close

        else:
            raise Exception ("Email ou Nome já cadastrados")
    

        
    def logar(self):

        user = self._verifica_existencia_usuario() 
       
        if user:
            if user['senha'] == self.senha:
                self.nome = user['nome']
                session['logedin'] = True
                session['usuario'] = {"nome":self.nome, "email":self.email, "id": user['id']}
                
            else: 
                raise Exception ("Email ou senha incorretos!")
        else:
            raise Exception ("Email ou senha incorretos!")

      
