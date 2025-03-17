#DICCIONARIO
def obtener_divisas
  {
    'Dollar' => '$',
    'Euro' => '€',
    'Yen' => '¥',
    'Peso' => '$'
  }
end

def conversor
  divisas = obtener_divisas
  
  loop do
    print "Ingrese el tipo de divisa (o 'salir' para terminar): "
    divisa = gets.chomp.capitalize
    
    if divisa.downcase == 'salir'
      puts "Gracias por usar el conversor de divisas. ¡Hasta luego!"
      break
    end
    
    if divisas.key?(divisa)
      puts "Esta es la divisa: #{divisas[divisa]}"
    else
      puts "Divisa no encontrada. Por favor, intenta de nuevo."
    end
  end
end

conversor
