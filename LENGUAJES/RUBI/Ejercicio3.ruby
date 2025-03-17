#CAJERO
def mostrar_menu
  puts "\nBienvenido al cajero"
  puts "1. Ingresar dinero"
  puts "2. Retirar dinero"
  puts "3. Ver saldo"
  puts "4. Salir"
end

def obtener_monto(mensaje)
  loop do
    print mensaje
    input = gets.chomp
    begin
      monto = Float(input)
      if monto < 0
        puts "El monto debe ser un número positivo. Inténtalo de nuevo."
      else
        return monto
      end
    rescue ArgumentError
      puts "Error, por favor ingrese un número válido."
    end
  end
end

def cajero
  saldo = 1000.0
  loop do
    mostrar_menu
    print "¿Qué deseas hacer? "
    opcion = gets.chomp
    
    case opcion
    when "1"
      monto = obtener_monto("¿Cuánto dinero deseas ingresar? $")
      saldo += monto
      puts "Se ha ingresado $#{'%.2f' % monto} a tu cuenta. Tu saldo actual es $#{'%.2f' % saldo}."
    
    when "2"
      monto = obtener_monto("¿Cuánto dinero deseas retirar? $")
      if monto <= saldo
        saldo -= monto
        puts "Se ha retirado $#{'%.2f' % monto} de tu cuenta. Tu saldo actual es $#{'%.2f' % saldo}."
      else
        puts "Error: No tienes suficiente saldo para realizar esta operación."
      end
    
    when "3"
      puts "Tu saldo actual es $#{'%.2f' % saldo}."
    
    when "4"
      puts "Gracias por utilizar el cajero."
      break
    
    else
      puts "Opción no válida. Por favor, intenta de nuevo."
    end
  end
end

cajero