from peewee import MySQLDatabase, Model, DatabaseError
import os
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv('DB_PASSWORD')

database = MySQLDatabase(
    'student_registration_system',  
    user='root',  
    password=db_password,  
    host='localhost',  
    port=3306,  
)

class BaseModel(Model):
    class Meta:
        database = database

def conectar() -> None:
    database.connect()

def criar_tabelas() -> None: 
    from app.models import Aluno, Nota, Disciplina
    try:
        database.create_tables([Aluno, Nota, Disciplina], safe=True)
    except DatabaseError as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        database.close()