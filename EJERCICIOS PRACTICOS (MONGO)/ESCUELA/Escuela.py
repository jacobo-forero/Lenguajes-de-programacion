from pymongo import MongoClient
from bson.son import SON

client = MongoClient('mongodb://localhost:27017/')
db = client.escuela

estudiantes_collection = db.estudiantes

estudiantes = [
    {"nombre": "Ana", "edad": 20, "curso": "Matemáticas", "nota": 9.0},
    {"nombre": "Luis", "edad": 21, "curso": "Física", "nota": 7.5},
    {"nombre": "Pedro", "edad": 22, "curso": "Matemáticas", "nota": 8.5},
    {"nombre": "María", "edad": 20, "curso": "Química", "nota": 6.0},
    {"nombre": "Juan", "edad": 19, "curso": "Física", "nota": 5.5}
]

estudiantes_collection.insert_many(estudiantes)

# 1. Encontrar todos los estudiantes que tienen una nota mayor a 8
estudiantes_mayor_8 = list(estudiantes_collection.find({"nota": {"$gt": 8}}))
print("Estudiantes con nota mayor a 8:", estudiantes_mayor_8)
print(' ')

# 2. Encontrar los estudiantes que tienen 20 años
estudiantes_20 = list(estudiantes_collection.find({"edad": 20}))
print("Estudiantes de 20 años:", estudiantes_20)
print(' ')

# 3. Actualizar la nota de "Ana" a 9.5
estudiantes_collection.update_one({"nombre": "Ana"}, {"$set": {"nota": 9.5}})


# 4. Incrementar la edad de todos los estudiantes en 1 año
estudiantes_collection.update_many({}, {"$inc": {"edad": 1}})

# 5. Encontrar los estudiantes que tienen una nota entre 7 y 9 y tienen menos de 22 años
estudiantes_rango_nota = list(estudiantes_collection.find({"nota": {"$gte": 7, "$lte": 9}, "edad": {"$lt": 22}}))
print("Estudiantes con nota entre 7 y 9 y menos de 22 años:", estudiantes_rango_nota)
print(' ')

# 6. Calcular el promedio de las notas de todos los estudiantes
promedio_notas = estudiantes_collection.aggregate([
    {"$group": {"_id": None, "promedio": {"$avg": "$nota"}}}
])
promedio = list(promedio_notas)[0]['promedio']
print("Promedio de notas:", promedio)
print(' ')

# 7. Agrupar los estudiantes por curso y calcular la nota promedio por curso
promedio_por_curso = estudiantes_collection.aggregate([
    {"$group": {"_id": "$curso", "promedio_nota": {"$avg": "$nota"}}}
])
print("Promedio de notas por curso:")
for curso in promedio_por_curso:
    print(curso)
    print(' ')

# 8. Crear un índice en el campo curso
estudiantes_collection.create_index("curso")

# Explicación sobre el índice
print("Índice creado en el campo 'curso'. Esto mejora el rendimiento de las consultas que filtran o agrupan por este campo.")
print(' ')

# 9. Realizar una consulta que utilice el índice creado
estudiantes_por_curso = list(estudiantes_collection.find({"curso": "Matemáticas"}))
print("Estudiantes en el curso de Matemáticas:", estudiantes_por_curso)
print(' ')

# 10. Eliminar todos los estudiantes que tienen una nota menor a 6
estudiantes_collection.delete_many({"nota": {"$lt": 6}})

# 11. Crear una colección cursos donde cada documento contenga un arreglo de estudiantes inscritos
cursos_collection = db.cursos
cursos = [
    {"curso": "Matemáticas", "estudiantes": ["Ana", "Pedro"]},
    {"curso": "Física", "estudiantes": ["Luis"]},
    {"curso": "Química", "estudiantes": ["María"]}
]
cursos_collection.insert_many(cursos)

# 12. Encontrar todos los cursos en los que está inscrito un estudiante específico
estudiante_especifico = "Ana"
cursos_inscritos = list(cursos_collection.find({"estudiantes": estudiante_especifico}))
print(f"Cursos en los que está inscrita {estudiante_especifico}:", cursos_inscritos)
print(' ')

client