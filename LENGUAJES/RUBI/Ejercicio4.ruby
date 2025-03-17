#CICLO FOR

def obtener_float(mensaje)
  loop do
    print mensaje
    input = gets.chomp
    begin
      valor = Float(input)
      if valor < 0
        puts "El valor debe ser un número positivo. Inténtalo de nuevo."
      else
        return valor
      end
    rescue ArgumentError
      puts "Error, por favor ingrese un número válido."
    end
  end
end

def obtener_int(mensaje)
  loop do
    print mensaje
    input = gets.chomp
    begin
      valor = Integer(input)
      if valor < 0
        puts "El valor debe ser un número entero positivo. Inténtalo de nuevo."
      else
        return valor
      end
    rescue ArgumentError
      puts "Error, por favor ingrese un número válido."
    end
  end
end

def inversion
  cant = obtener_float("Ingrese la cantidad a invertir: $")
  inter = obtener_float("Ingrese el interés anual (en %): ")
  años = obtener_int("Ingrese el número de años: ")
  
  puts "\nResumen de la inversión:"
  (1..años).each do |i|
    cant += cant * (inter / 100)
    puts "Año #{i}: Capital obtenido será: $#{'%.2f' % cant}"
  end
end

inversion