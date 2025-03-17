require 'mysql2'

begin
    client = Mysql2::Client.new(:host => "localhost", :username => "root", :password => "")
    puts "Conexión exitosa"
rescue Mysql2::Error => e
    puts e.message
ensure
    client.close if client
end