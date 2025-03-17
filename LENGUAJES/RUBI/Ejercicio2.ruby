#BUCLE WHILE

def obtener_numero
  loop do
    print "Ingrese un número para conocer la tabla de multiplicar: "
    input = gets.chomp
    begin
      num = Integer(input)
      return num
    rescue ArgumentError
      puts "Error, por favor ingrese un número entero."
    end
  end
end

def mostrar_tabla(num)
  puts "\nTabla de multiplicar del #{num}:"
  (1..10).each do |i|
    puts "#{num} x #{i} = #{num * i}"
  end
end

def main
  loop do
    numero = obtener_numero
    mostrar_tabla(numero)

    print "\n¿Desea calcular otra tabla? (s/n): "
    continuar = gets.chomp.strip.downcase
    if continuar != 's'
      puts "Gracias por usar el programa. ¡Hasta luego!"
      break
    end
  end
end

main