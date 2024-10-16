from app.models import Aluno, Disciplina
from app.dao.nota_dao import NotaDAO

class NotaService:

    def adicionar_nota(self, id_aluno, id_disciplina, nota_1, nota_2):
        if self.validar_nota(nota_1) and self.validar_nota(nota_2):
            if self.validar_aluno(id_aluno) and self.validar_disciplina(id_disciplina):
                try:
                    aluno = Aluno.get(Aluno.id == id_aluno)
                    disciplina = Disciplina.get(Disciplina.id == id_disciplina)
                    nota = NotaDAO.criar_nota(aluno, disciplina, nota_1, nota_2)
                    return f"Nota adicionada com sucesso para o aluno '{aluno.nome} na disciplina '{disciplina.nome}'"
                except Exception as e:
                    return f'Erro ao adicionar nota: {str(e)}'
            else:
                return 'Aluno ou disciplina inválidos'
        else:
            return 'Notas inválidas'
        
    def buscar_nota(self, id_nota):
        try:
            nota = NotaDAO.buscar_nota(id_nota)
            if nota:
                return nota
            return 'Nota não encontrada'
        except Exception as e:
            return f'Erro ao buscar nota {str(e)}'
        
    def deletar_nota(self, id_nota):
        try:
            nota_deletada = NotaDAO.deletar_nota(id_nota)
            if nota_deletada:
                return 'Nota deletado com sucesso.'
            return 'Nota não encontrada.'
        except Exception as e:
            return f'Erro ao deletar nota: {str(e)}'
        
    def listar_notas(self):
        try:
            notas = NotaDAO.listar_notas()
            if notas:
                return notas
            return 'Nenhuma nota encontrada.'
        except Exception as e:
            return Exception(f'Erro ao listar notas: {str(e)}')

    def calcular_media(self, nota_1, nota_2):

        if not isinstance(nota_1, (int, float)) or not isinstance(nota_2, (int, float)):
            return 'Erro: As notas devem ser um número.'
        
        if nota_1 < 0 or nota_1 > 10 or nota_2 < 0 or nota_2 > 10:
            return 'Erro: As notas devem estar entre 0 e 10.'
        
        return (nota_1 + nota_2) / 2
    
    def status_aprovacao(self, media):
            
        if not isinstance(media, (int, float)):
            return 'Erro: A média deve ser um número.'
        
        if media < 0 or media > 10:
            return 'Erro: A média deve estar entre 0 e 10.'
        
        return 'Aprovado' if media >= 7 else 'Reprovado'
    

    def validar_nota(self, nota):
        return isinstance(nota, (int,float)) and 0 <= nota <= 10
    
    def validar_aluno(self, id_aluno):
        return Aluno.select().where(Aluno.id == id_aluno).exists()
    
    def validar_disciplina(self, id_disciplina):
        return Disciplina.select().where(Disciplina.id == id_disciplina).exists() 