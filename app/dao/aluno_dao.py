from app.models import Aluno

class AlunoDAO():
    @staticmethod
    def criar_aluno(nome, idade, curso, matricula):
        try:
            aluno = Aluno.create(nome=nome, idade=idade, curso=curso, matricula=matricula)
            return aluno
        except Exception as e:
            raise Exception(f'Erro ao criar aluno: {e}')

    @staticmethod
    def buscar_aluno( id_aluno):
        try:
            aluno = Aluno.get(Aluno.id == id_aluno)
            return aluno
        except Aluno.DoesNotExist:
            return None
        except Exception as e:
            raise Exception(f'Erro ao buscar aluno: {e}')

    
    @staticmethod
    def deletar_aluno(id_aluno):
        try:
            aluno = Aluno.get(Aluno.id == id_aluno)
            aluno.delete_instance()
            return True
        except Aluno.DoesNotExist:
            return False
        except Exception as e:
            raise Exception(f'Erro ao deletar aluno: {e}')


    @staticmethod
    def listar_alunos():
        try:
            alunos = Aluno.select()
            return list(alunos)
        except Exception as e:
            raise Exception(f'Erro ao listar alunos: {e}')