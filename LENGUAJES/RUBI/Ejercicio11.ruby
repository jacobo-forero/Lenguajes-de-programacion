#OPERACIONES

def suma(num1, num2)
  num1 + num2
end

def resta(num1, num2)
  num1 - num2
end

def multiplicacion(num1, num2)
  num1 * num2
end

def division(num1, num2)
  if num2 != 0
    num1 / num2
  else
    "No se puede dividir entre cero"
  end
end

def potencia(num1, num2)
  num1 ** num2
end

def main
  loop do
    puts "\nCalculadora"
    puts "1. Suma"
    puts "2. Resta"
    puts "3. Multiplicación"
    puts "4. División"
    puts "5. Potencia"
    puts "6. Salir"

    print "Selecciona una opción (1-6): "
    opcion = gets.chomp

    if opcion == '6'
      puts "Gracias por usar la calculadora. ¡Hasta luego!"
      break
    end

    print "Ingresa el primer número: "
    num1 = gets.chomp.to_f
    print "Ingresa el segundo número: "
    num2 = gets.chomp.to_f

    case opcion
    when '1'
      puts "Resultado de la suma: #{suma(num1, num2)}"
    when '2'
      puts "Resultado de la resta: #{resta(num1, num2)}"
    when '3'
      puts "Resultado de la multiplicación: #{multiplicacion(num1, num2)}"
    when '4'
      resultado = division(num1, num2)
      puts "Resultado de la división: #{resultado}"
    when '5'
      puts "Resultado de la potencia: #{potencia(num1, num2)}"
    else
      puts "Opción no válida. Por favor, selecciona una opción del 1 al 6."
    end
  end
end

main