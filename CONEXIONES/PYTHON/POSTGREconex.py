import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "1234"
)

print(conn)
print("Conexion exitosa")