from peewee import CharField, IntegerField, ForeignKeyField, FloatField
from db.database import BaseModel

class Aluno(BaseModel):
    nome = CharField()
    idade = IntegerField()
    curso = CharField()
    matricula = CharField(unique=True)

class Disciplina(BaseModel):
    nome = CharField()
    codigo = CharField(unique=True)
    carga_horario = IntegerField()
    professor = CharField()

class Nota(BaseModel):
    aluno = ForeignKeyField(Aluno, backref='notas')
    disciplina = ForeignKeyField(Disciplina, backref='notas')
    nota_1 = FloatField()
    nota_2 = FloatField()



