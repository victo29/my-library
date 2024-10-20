from flask_login import UserMixin
from hashlib import sha256
from sqlalchemy import Column, Integer, String
from models.conection import Base, SessionLocal
from sqlalchemy.orm import relationship
import bleach


class Usuario(Base, UserMixin):  
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(64))  


    def __init__(self, email: str, password: str, name: str = "Default") -> None:
        self.name = bleach.clean(name)
        self.email = bleach.clean(email)
        self.password = self._hash_password(password)

    # publicacoes = relationship("Publicacao", back_populates="usuario")

    # Criptografa as senhas passadas
    @staticmethod
    def _hash_password(password: str) -> str:
        
        return sha256(password.encode()).hexdigest()
    
    # Verifica se existe um usuário com o email passado
    def _verify_if_exist_user(self):
        
        with SessionLocal() as session:
            return session.query(Usuario).filter(Usuario.email == self.email).first()
        
    # Realiza o cadastro dos usuários
    def register(self) -> bool | Exception:
        
        if not self._verify_if_exist_user():
            with SessionLocal() as session:
                session.add(self)
                session.commit()
            return True
        else:
            raise Exception("Email já cadastrados")

    # Realiza o login dos usuários
    def login(self) -> bool | Exception:
        
        user = self._verify_if_exist_user()
        if user and user.password == self.password:
            self.name = user.name
            self.id = user.id  
            return user  
        else:
            raise Exception("Email ou senha incorretos!")
    
    def get_id(self):
       
        return str(self.id)  
