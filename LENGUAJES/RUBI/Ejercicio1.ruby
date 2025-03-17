# BUCLES FOR
def mostrar_palabra
  print "Ingrese la palabra que quiere que se repita: "
  palabra = gets.chomp.strip

  while palabra.empty?
    puts "La entrada no puede estar vacía. Inténtalo de nuevo."
    print "Ingrese la palabra que quiere que se repita: "
    palabra = gets.chomp.strip
  end
  
  repeticiones = 0
  loop do
    print "¿Cuántas veces quiere que se repita la palabra? "
    input = gets.chomp
    if input.match?(/^\d+$/) 
      repeticiones = input.to_i
      if repeticiones > 0
        break
      else
        puts "Por favor, ingrese un número positivo."
      end
    else
      puts "Entrada no válida. Por favor, ingrese un número entero."
    end
  end
  
  repeticiones.times { puts palabra }
end

mostrar_palabra