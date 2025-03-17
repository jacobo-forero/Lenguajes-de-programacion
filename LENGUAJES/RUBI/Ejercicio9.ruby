#LEY OHM
def obtener_float(mensaje)
  loop do
    print mensaje
    input = gets.chomp
    begin
      valor = Float(input)
      if valor < 0
        puts "El valor no puede ser negativo. Inténtalo de nuevo."
      else
        return valor
      end
    rescue ArgumentError
      puts "Error: Debes ingresar un número válido."
    end
  end
end

def calcular_ley_ohm
  puts "Calculadora de la Ley de Ohm"
  
  loop do
    puts "\nSelecciona la variable que deseas calcular:"
    puts "1. Voltaje (V)"
    puts "2. Corriente (I)"
    puts "3. Resistencia (R)"
    puts "4. Salir"

    opcion = gets.chomp

    case opcion
    when '1'
      I = obtener_float("Ingresa la corriente (I) en amperios: ")
      R = obtener_float("Ingresa la resistencia (R) en ohmios: ")
      V = I * R
      puts "El voltaje (V) es: #{'%.2f' % V} voltios"

    when '2'
      V = obtener_float("Ingresa el voltaje (V) en voltios: ")
      R = obtener_float("Ingresa la resistencia (R) en ohmios: ")
      I = V / R
      puts "La corriente (I) es: #{'%.2f' % I} amperios"

    when '3'
      V = obtener_float("Ingresa el voltaje (V) en voltios: ")
      I = obtener_float("Ingresa la corriente (I) en amperios: ")
      R = V / I
      puts "La resistencia (R) es: #{'%.2f' % R} ohmios"

    when '4'
      puts "Gracias por usar la calculadora de la Ley de Ohm. ¡Hasta luego!"
      break

    else
      puts "Opción no válida. Por favor, selecciona 1, 2, 3 o 4."
    end
  end
end

calcular_ley_ohm