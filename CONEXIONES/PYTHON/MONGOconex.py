import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017")
print(cliente)
print("Conexion  exitosa")