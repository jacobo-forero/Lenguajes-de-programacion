#TABLA DE LA VERDAD
def generar_combinaciones(variables)
  variables.map { |var| [true, false] }.reduce(&:product)
end

def imprimir_tabla_verdad(variables)
  combinaciones = generar_combinaciones(variables)
  
  puts "#{variables.join(' | ')} | #{variables.join(' y ')}"
  puts "-" * (variables.length * 4 + 10)

  combinaciones.each do |combinacion|
    resultado = combinacion.all?  # A y B
    puts "#{combinacion.join(' | ')} | #{resultado}"
  end
end

def main
  variables = ['A', 'B']
  imprimir_tabla_verdad(variables)
end

main