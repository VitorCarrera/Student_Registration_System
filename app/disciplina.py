from app.models import Disciplina
from app.dao.disciplina_dao import DisciplinaDAO
from random import randint

class DisciplinaService:

    def criar_disciplina(self, nome, professor, carga_horaria):
        if self.validar_disciplina(nome, professor, carga_horaria):
            codigo = self.gerar_codigo(nome)
            
            try:
                disciplina = DisciplinaDAO.criar_disciplina(nome, codigo, professor, carga_horaria)
                return f"Disciplina '{disciplina.nome}' criada com sucesso."
            except Exception as e:
                return f"Erro ao criar disciplina: {str(e)}"
        else:
             return 'Dados inválidos para criar disciplina.'

    def buscar_disciplina(self, codigo):
        try:
            disciplina = DisciplinaDAO.buscar_disciplina(codigo)
            if disciplina:
                return disciplina
            return 'Disciplina não encontrada.'
        except Exception as e:
            return f'Erro ao buscar disciplina: {str(e)}'

    def deletar_disciplina(self, codigo):
        try:
            disciplina_deletada = DisciplinaDAO.deletar_disciplina(codigo)
            if disciplina_deletada:
                return 'Disciplina deletada com sucesso.'
            return 'Disciplina não encontrada.'
        except Exception as e:
            return f'Erro ao deletar disciplina: {str(e)}'

    def listar_disciplinas(self):
        try:
            disciplinas = DisciplinaDAO.listar_disciplinas()
            if disciplinas:
                return disciplinas
            return 'Nenhuma disciplina encontrada'
        except Exception as e:
            return f'Erro ao listar disciplinas: {str(e)}'

    def gerar_codigo(self, nome):
            prefixo = nome.strip()[:3].upper()
            sufixo = str(randint(100,999))
            return f'{prefixo}-{sufixo}'
  
    def validar_disciplina(self, nome, professor, carga_horaria):
        return len(nome.strip()) > 0 and len(professor.strip()) > 0 and carga_horaria > 0