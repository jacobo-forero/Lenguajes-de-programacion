#FUNCIONES
def obtener_nombre
  loop do
    print "Ingrese su nombre: "
    nombre = gets.chomp.strip
    if !nombre.empty?
      return nombre
    else
      puts "El nombre no puede estar vacío. Inténtalo de nuevo."
    end
  end
end

def saludo(nombre)
  puts "Hola #{nombre}, bienvenido/a!"
end

def main
  loop do
    nombre = obtener_nombre
    saludo(nombre)
    
    print "¿Deseas saludar a otra persona? (s/n): "
    continuar = gets.chomp.strip.downcase
    if continuar != 's'
      puts "Gracias por usar el programa. ¡Hasta luego!"
      break
    end
  end
end

main