#Condicionales IF, ELSE
def obtener_edad
  loop do
    print "Ingresa tu edad: "
    input = gets.chomp
    begin
      edad = Integer(input)
      if edad < 0
        puts "La edad no puede ser negativa. Inténtalo de nuevo."
      else
        return edad
      end
    rescue ArgumentError
      puts "Error, por favor ingresa un número entero válido."
    end
  end
end

def mayoria_edad
  edad = obtener_edad
  
  if edad >= 18
    puts "Eres mayor de edad."
  else
    puts "Eres menor de edad."
  end
end

mayoria_edad