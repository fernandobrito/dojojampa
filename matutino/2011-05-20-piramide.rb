# 3ª Sessão DojoJampa Matutino - 20 de maio de 2011
# http://dojojampa.posterous.com
#
# Problema: Após uma guerra sangrenta, os soldados se entediaram e resolveram
# construir pirâmides com as cabeças dos mortos para passar o tempo.
# Eles detestavam coisas inacabadas e decidiram que só iriam começar a construir
# pirâmides se soubessem a  quantidade total de cabeças que iriam precisar.
#
# A sua tarefa é fazer um programa cuja entrada seja a quantidade de cabeças
# por lado na base da pirâmide e cuja saída seja a quantidade total de cabeças
# para se construir a pirâmide toda.
# 
# Cada etapa superior da pirâmide possui uma cabeça a menos por lado.
#
# Ex: Entrada: 3 (cabeças por lado na base do triângulo)
#
# Base: 3 cabeças por lado
# 1o andar: 2 cabeças por lado
# 2o andar: 1 cabeça por lado
#
# Na base, temos:   *
#                  * *
#                 * * *
#
# Para fazer a base, precisamos de 6 cabeças.
# No primeiro andar, precisamos de 3, e no segundo (topo) apenas 1.
# A saída deve ser a soma, que é: 10 cabeças.
#
# (Problema modificado da OPI 2011 - Categoria Avançado)
#
# Status: Resolvido

require "test/unit"

def cabecas_por_nivel(cabecas_por_lado)
  total_nivel = 0
  (cabecas_por_lado).times do |i|
    total_nivel = total_nivel + (i + 1)
  end

  return total_nivel
end

def resultado(cabecas_por_lado)
    total_cabecas = 0

  (cabecas_por_lado).times do |n|
    cabecas_por_camada = cabecas_por_nivel(n + 1)
    total_cabecas = total_cabecas + cabecas_por_camada
  end

  return total_cabecas

end



class TestDojo < Test::Unit::TestCase
  def test_cabecas_por_nivel
    assert_equal(1, cabecas_por_nivel(1))
    assert_equal(3, cabecas_por_nivel(2))
    assert_equal(6, cabecas_por_nivel(3))
  end
  def test_resultado
    assert_equal(4, resultado(2))
    assert_equal(10, resultado(3))
    assert_equal(20, resultado(4))
  end

end
