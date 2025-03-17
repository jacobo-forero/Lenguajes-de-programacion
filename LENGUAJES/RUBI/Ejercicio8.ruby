#INTERACCION CON EL USUARIO
def obtener_adivinanza
  loop do
    print "Adivina el número del 1 al 10: "
    input = gets.chomp
    begin
      adivinar = Integer(input)
      if (1..10).include?(adivinar)
        return adivinar
      else
        puts "Por favor, ingresa un número entre 1 y 10."
      end
    rescue ArgumentError
      puts "Error: Debes ingresar un número entero."
    end
  end
end

def jugar
  num = rand(1..10)
  intentos = 3  # Número de intentos permitidos

  puts "Tienes 3 intentos para adivinar el número."
  
  (0...intentos).each do |i|
    adivinar = obtener_adivinanza
    
    if num == adivinar
      puts "¡Has ganado!"
      return
    else
      puts "Intento #{i + 1} fallido."
    end
  end

  puts "Has perdido, el número era: #{num}"
end

def main
  loop do
    jugar
    print "¿Quieres jugar de nuevo? (s/n): "
    continuar = gets.chomp.strip.downcase
    if continuar != 's'
      puts "Gracias por jugar. ¡Hasta luego!"
      break
    end
  end
end

main