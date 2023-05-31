# Crie uma instância da classe Database, substituindo os valores de URI, usuário e senha pelos corretos
from teacherCRUD import TeacherCRUD
from database import Database

database = Database("bolt://44.197.247.118:7687","neo4j", "topping-oxides-probabilities")

teacher_crud = TeacherCRUD(database)

teacher_crud.create('Chris Lima', 1956, '189.052.396-66')

teacher = teacher_crud.read('Chris Lima')

if teacher:
    print(f"Professor encontrado: {teacher}")
else:
    print("Professor não encontrado.")

teacher_crud.update('Chris Lima', '162.052.777-77')

print("CPF do professor atualizado com sucesso.")