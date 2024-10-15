from app.models import Disciplina

class DisciplinaDAO():
    @staticmethod
    def criar_disciplina(nome, codigo, professor, carga_horaria):
        try:
            disciplina = Disciplina.create(nome=nome, codigo=codigo, professor=professor, carga_horaria=carga_horaria)
            return disciplina
        except Exception as e:
            raise Exception(f'Erro ao criar disciplina: {e}')
        
    @staticmethod
    def buscar_disciplina(codigo):
        try:
            disciplina = Disciplina.get(Disciplina.codigo == codigo)
            return disciplina
        except Disciplina.DoesNotExist:
            return None
        except Exception as e:
            raise Exception(f'Erro ao buscar disciplina: {e}')

    @staticmethod
    def deletar_disciplina(codigo):
        try:
            disciplina = Disciplina.get(Disciplina.codigo == codigo)
            Disciplina.delete_instance(disciplina)
            return True
        except Disciplina.DoesNotExist:
            return False
        except Exception as e:
            raise Exception(f'Erro ao deletar disciplina: {e}')
        
    @staticmethod
    def listar_disciplinas():
        try: 
            disciplinas = Disciplina.select()
            return list(disciplinas)
        except Exception as e:
            raise Exception(f'Erro ao listar disciplinas: {e}')