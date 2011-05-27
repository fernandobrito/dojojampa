# 1ª Sessão DojoJampa Noturno - 11 de maio de 2011
# http://dojojampa.posterous.com
#
# Problema: http://dojopuzzles.com/problemas/exibe/encontre-o-telefone/ 
# Link blog: http://dojojampa.posterous.com/dojojampa-11-de-maio-de-2011/
#
# Status: Resolvido

require "test/unit"

def convertion(input)
  case input
    when "A", "B", "C": return "2"
    when "D", "E", "F": return "3"
    when "G", "H", "I": return "4"
    when "J", "K", "L": return "5"
    when "M", "N", "O": return "6"
    when "P", "Q", "R", "S": return "7"
    when "T", "U", "V": return "8"
    when "W", "X", "Y", "Z": return "9"
    else return input
  end
end

def union(string)
  converted = ""

  string.each_char do |c|
    converted << convertion(c)
  end

  return converted
end



class TestDojo < Test::Unit::TestCase

  def test_convertion
    assert_equal("2", convertion("A"))
    assert_equal("2", convertion("B"))
    assert_equal("2", convertion("C"))
    assert_equal("3", convertion("D"))
    assert_equal("4", convertion("G"))
    assert_equal("5", convertion("L"))
    assert_equal("6", convertion("M"))
    assert_equal("7", convertion("P"))
    assert_equal("8", convertion("T"))
    assert_equal("9", convertion("W"))

    assert_equal("1", convertion("1"))
    assert_equal("-", convertion("-"))
  end

  def test_union()
    assert_equal("1-4663-79338-4663", union("1-HOME-SWEET-HOME"))
    assert_equal("83-2526-0001", union("83-ALAN-0001"))
  end

end
