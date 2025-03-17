#LISTAS
def mostrar(materias)
  if !materias.empty?
    puts "Yo estudio #{materias.length} materias."
    puts "Las materias son:"
    materias.each do |materia|
      puts "- #{materia}"
    end
  else
    puts "No hay materias para mostrar."
  end
end

def agregar_materia(materias)
  print "Ingresa el nombre de la nueva materia: "
  nueva_materia = gets.chomp.strip
  if !nueva_materia.empty?
    materias << nueva_materia
    puts "La materia '#{nueva_materia}' ha sido agregada."
  else
    puts "El nombre de la materia no puede estar vacío."
  end
end

def main
  lista = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
  mostrar(lista)

  loop do
    print "¿Deseas agregar una nueva materia? (s/n): "
    continuar = gets.chomp.strip.downcase
    if continuar == 's'
      agregar_materia(lista)
      mostrar(lista)
    elsif continuar == 'n'
      puts "Gracias por usar el programa. ¡Hasta luego!"
      break
    else
      puts "Opción no válida. Por favor, ingresa 's' o 'n'."
    end
  end
end

main