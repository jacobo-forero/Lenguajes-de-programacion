require 'mongo'

client = Mongo::Client.new('mongodb://localhost:27017')

puts "Conexión exitosa"