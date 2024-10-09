from app.models import Disciplina

class DisciplinaService:

    def validar_disciplina(self, nome, professor, carga_horaria):
        return len(nome.strip()) > 0 and len(professor.strip()) > 0 and carga_horaria > 0