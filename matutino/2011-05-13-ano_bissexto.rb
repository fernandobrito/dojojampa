# 2ª Sessão DojoJampa Matutino - 13 de maio de 2011
# http://dojojampa.posterous.com
#
# Problema: http://dojopuzzles.com/problemas/exibe/ano-bissexto/
#
# Status: Resolvido

require "test/unit"

def ano_bissexto(n1)
  if n1%400 ==0
    return 1


  elsif n1 %4==0 and n1%100 != 0
    return 1
  end
 return 0

end



class TestDojo < Test::Unit::TestCase

  def test_not400_div100_div4
    assert_equal(0, ano_bissexto(1900))
  end
  def test_falso
    assert_equal(0, ano_bissexto(1997))
  end
  def test_div_not100
    assert_equal(1, ano_bissexto(2008))
  end
  def test_div4_div400_div100
    assert_equal(1, ano_bissexto(2000))
  end
  def test_site_verdadeiro
    assert_equal(1, ano_bissexto(1600))
    assert_equal(1, ano_bissexto(1732))
    assert_equal(1, ano_bissexto(1888))
    assert_equal(1, ano_bissexto(1944))
  end
  def test_site_falso
    assert_equal(0, ano_bissexto(1742))
    assert_equal(0, ano_bissexto(1889))
    assert_equal(0, ano_bissexto(1951))
    assert_equal(0, ano_bissexto(2011))
  end
end
