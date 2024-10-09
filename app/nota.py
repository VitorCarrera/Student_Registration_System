from app.models import Nota

class NotaService:

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