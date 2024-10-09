from app.models import Aluno
import random

class AlunoService:
    def gerar_matricula(self, nome):
        prefixo = nome[:3].upper()
        sufixo = str(random.randint(1000, 9999))
        return f'{prefixo}-{sufixo}'
    
    def validar_nome(self, nome):
        return isinstance(nome, str) and len(nome.strip) > 0

    def validar_curso(self, curso):
        return isinstance(curso, str) and len(curso.strip()) > 0