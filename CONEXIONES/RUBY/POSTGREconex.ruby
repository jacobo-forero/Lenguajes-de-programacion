require 'pg'

begin
    conn = PG.connect(host: 'localhost', dbname: 'tu_base_de_datos', user: 'postgres', password: '1234')
    puts "Conexión exitosa"
rescue PG::Error => e
    puts e.message
ensure
    conn.close if conn
end