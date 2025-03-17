#OCTAVOS DE FINAL
def simular_partido(equipo1, equipo2)
  [equipo1, equipo2].sample
end

def octavos_de_final(equipos)
  puts "Octavos de Final:"
  ganadores = []

  if equipos.length.odd?
    puts "El número de equipos debe ser par."
    return
  end

  equipos.each_slice(2) do |equipo1, equipo2|
    ganador = simular_partido(equipo1, equipo2)
    ganadores << ganador
    puts "Partido: #{equipo1} vs #{equipo2} - Ganador: #{ganador}"
  end

  ganadores
end

def main
  equipos = [
    "FC Barcelona",
    "Real Madrid",
    "Arsenal",
    "Manchester City",
    "Chelsea",
    "Liverpool",
    "PSG",
    "Benfica"
  ]

  ganadores = octavos_de_final(equipos)

  puts "\nEquipos que avanzan a los cuartos de final:"
  ganadores.each { |ganador| puts ganador }
end

main