# 2ª Sessão DojoJampa Matutino - 13 de maio de 2011
# http://dojojampa.posterous.com
#
# Problema: http://dojopuzzles.com/problemas/exibe/numeros-felizes/
#
# Status: Resolvido

require "test/unit"

def quadrado_de(numero)
  numero ** 2
end

def separar(n)
  string = n.to_s
  string = string.split("")
  resultado = []

  for item in string
    resultado << item.to_i
  end

  return resultado
end

def quadrado_lista(resultado)
  resultquad = []
  for item in resultado
    resultquad << quadrado_de(item)
  end

  return resultquad
end

def soma_itens(lista)
  soma = 0
  for item in lista
    soma = soma + item
  end

  return soma
end


def feliz(numero)
  puts 'Testando o número: ' + numero.to_s

  begin
    lista_ss = separar(numero) # lista de strings separados
    lista_quads = quadrado_lista(lista_ss)  # lista de quadrados
    resultado = soma_itens(lista_quads)
    numero = resultado

    puts resultado.to_s

    if [0, 4, 8, 9].include?(resultado)
      puts "Este numero é triste"
      return 0
    end
  end while(resultado != 1)

  puts "este numero é feliz"
  return resultado
end

class TestDojo < Test::Unit::TestCase
  def test_quadrado_de_numero
    assert_equal(49, quadrado_de(7))
  end

  def teste_separar
    assert_equal([3, 2, 1], separar(321))
    assert_equal([1], separar(1))
  end

  def teste_quadrado_lista
    assert_equal([16, 81], quadrado_lista([4, 9]))
    assert_equal([9, 25, 144], quadrado_lista([3, 5, 12]))
  end

  def test_soma_itens
    assert_equal(10, soma_itens([9, 1]))
    assert_equal(5, soma_itens([5]))
  end

  def test_feliz
    assert_equal(1, feliz(100))
    assert_equal(1, feliz(7))
    assert_equal(1, feliz(130))
    assert_equal(1, feliz(49))
  end

  def test_triste
    assert_equal(0, feliz(123))
    assert_equal(0, feliz(17))
    assert_equal(0, feliz(11))
    assert_equal(0, feliz(111))
  end
end
