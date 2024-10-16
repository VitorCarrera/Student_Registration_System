from app.models import Aluno
import random
from app.dao.aluno_dao import AlunoDAO
from peewee import IntegrityError

class AlunoService:
    def criar_aluno(self, nome, idade, curso):
        if self.validar_nome(nome) and self.validar_curso(curso) and self.validar_idade(idade):
            matricula = self.gerar_matricula(nome)

            try:
                aluno = AlunoDAO.criar_aluno(nome, idade, curso, matricula)
                return f"Aluno '{aluno.nome}'criado com sucesso."
            except Exception as e:
                return f"Erro ao criar aluno: {str(e)}"
        else:
            return "Dados inválidos para criar aluno."

    def buscar_aluno(self, id_aluno):
        try:
            aluno = AlunoDAO.buscar_aluno(id_aluno)
            if aluno:
                return aluno
            return "Aluno não encontrado."
        except Exception as e:
            return f"Erro ao buscar aluno: {str(e)}"

    def deletar_aluno(self, id_aluno):
        try:
            aluno_deletado = AlunoDAO.deletar_aluno(id_aluno)
            if aluno_deletado:
                return "Aluno deletado com sucesso."
            return "Aluno não encontrado."
        except Exception as e:
            return f"Erro ao deletar aluno: {str(e)}"

    def listar_disciplinas(self):
        try:
            alunos = AlunoDAO.listar_alunos()
            if alunos:
                return alunos
            return 'Nenhum aluno encontrada'
        except Exception as e:
            return f'Erro ao listar alunos: {str(e)}'

    def gerar_matricula(self, nome):
        matricula = None
        while not matricula:
            try:
                prefixo = nome.strip()[:3].upper()
                sufixo = str(random.randint(1000, 9999))
                nova_matricula = f'{prefixo}-{sufixo}'

                if not Aluno.select().where(Aluno.matricula == nova_matricula).exists():
                    matricula = nova_matricula
            except IntegrityError:
                continue
        return matricula
    
    def validar_nome(self, nome):
        return isinstance(nome, str) and len(nome.strip()) > 0

    def validar_curso(self, curso):
        return isinstance(curso, str) and len(curso.strip()) > 0
    
    def validar_idade(self, idade):
        return isinstance(idade, int) and 0 < idade < 100