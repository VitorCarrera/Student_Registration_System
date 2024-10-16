from app.models import Nota
class NotaDAO:
    @staticmethod
    def criar_nota(aluno, disciplina, nota_1, nota_2):
        try:
            nota = Nota.create(aluno=aluno, disciplina=disciplina, nota_1=nota_1, nota_2=nota_2)
            return nota
        except Exception as e:
            raise Exception(f'Erro ao adicionar nota: {e}')
        
    @staticmethod
    def buscar_nota(id_aluno, id_disciplina):
        try:
            nota = Nota.select().where((Nota.aluno == id_aluno) & (Nota.disciplina == id_disciplina)).first()
            return nota
        except Exception as e:
            raise Exception(f'Erro ao buscar nota: {e}')
        
    @staticmethod
    def deletar_nota(id_nota):
        try: 
            nota = Nota.get(Nota.id == id_nota)
            nota.delete_instance()
            return True
        except Nota.DoesNotExist:
            return False
        except Exception as e:
            raise Exception(f'Erro ao deletar nota: {e}')
        

    @staticmethod
    def listar_notas():
        try:
            notas = Nota.select()
            return list(notas)
        except Exception as e:
            raise Exception(f'Erro ao listar notas: {e}')