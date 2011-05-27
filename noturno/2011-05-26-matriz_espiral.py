#!/usr/bin/env python
# encoding: utf-8
#
# 2ª Sessão DojoJampa Noturno - 26 de maio de 2011
# http://dojojampa.posterous.com
#
# Problema: http://dojopuzzles.com/problemas/exibe/matriz-espiral/

import unittest

class MatrizEspiral(object):
	def __init__(self,rows,columns):
		self.matrix=[ [ 0 for x in range(columns)] for y in range(rows)]
		self._sentido='direita'
		self._i=0
		self._j=0
		self._numero_final=rows*columns
	

	def muda_sentido(self):
		if(self._sentido == 'direita'):
			self._sentido ='baixo'
		elif(self._sentido == 'baixo'):
			self._sentido ='esquerda'
		elif(self._sentido == 'esquerda'):
			self._sentido ='cima'
		elif(self._sentido == 'cima'):
			self._sentido ='direita'
				

	def caminha_na_matriz(self):
		if len(self.matrix) == 0:
			return
			
		if 	 (self._sentido == 'direita' and 
			 self._j < len(self.matrix[self._i])-1 and
			 self.matrix[self._i][self._j+1]==0):
				self._j+=1
		elif (self._sentido == 'esquerda' and
		 	 self._j > 0 and
		 	 self.matrix[self._i][self._j-1]==0):
				self._j-=1
		elif (self._sentido == 'baixo' and 
			 self._i < len(self.matrix)-1 and
			 self.matrix[self._i+1][self._j]==0):
				self._i+=1
		elif (self._sentido == 'cima' and 
			 self._i > 0 and
			 self.matrix[self._i-1][self._j]==0):
				self._i-=1


	def preenche_espiral(self):
		if len(self.matrix) == 0: return
			
		numero=1
		while(numero<=self._numero_final) and self.matrix[self._i][self._j]==0:
			while len(self.matrix[self._i]) > 0 and self.matrix[self._i][self._j]==0:
				self.matrix[self._i][self._j]=numero
				numero+=1
				self.caminha_na_matriz()
			self.muda_sentido()
			self.caminha_na_matriz()




class MyTests(unittest.TestCase):
	def setUp(self):
		pass

	def test_create_matrix(self):
		m = MatrizEspiral(0,0)
		expected = []
		self.assertEquals(m.matrix,expected)

		m = MatrizEspiral(1,1)
		expected = [[0]]
		self.assertEquals(m.matrix,expected)

		m = MatrizEspiral(2,2)
		expected = [[0,0],[0,0]]
		self.assertEquals(m.matrix,expected)

		m = MatrizEspiral(2,3)
		expected = [[0,0,0],[0,0,0]]
		self.assertEquals(m.matrix,expected)

	def test_muda_sentido(self):
		m = MatrizEspiral(0,0)
		self.assertEquals(m._sentido,'direita')

		m.muda_sentido()
		self.assertEquals(m._sentido,'baixo')
		
		m.muda_sentido()
		self.assertEquals(m._sentido,'esquerda')

		m.muda_sentido()
		self.assertEquals(m._sentido,'cima')
		
		m.muda_sentido()
		self.assertEquals(m._sentido,'direita')


	def test_caminha_na_matriz(self):
		m = MatrizEspiral(2,2)
		self.assertEquals( (m._i,m._j), (0,0) )
		
		m.caminha_na_matriz()
		self.assertEquals( (m._i,m._j), (0,1) )

		m.muda_sentido()
		m.caminha_na_matriz()
		self.assertEquals( (m._i,m._j), (1,1) )

		m.muda_sentido()
		m.caminha_na_matriz()
		self.assertEquals( (m._i,m._j), (1,0) )

		m.muda_sentido()
		m.caminha_na_matriz()
		self.assertEquals( (m._i,m._j), (0,0) )
		
		
		m = MatrizEspiral(1,1)
		self.assertEquals( (m._i,m._j), (0,0) )
		
		m.caminha_na_matriz()
		self.assertEquals( (m._i,m._j), (0,0) )

		m.muda_sentido()
		m.caminha_na_matriz()
		self.assertEquals( (m._i,m._j), (0,0) )

		m.muda_sentido()
		m.caminha_na_matriz()
		self.assertEquals( (m._i,m._j), (0,0) )

		m.muda_sentido()
		m.caminha_na_matriz()
		self.assertEquals( (m._i,m._j), (0,0) )
		
				
		
	def test_preenche_espiral(self):
		m = MatrizEspiral(0,0)
		m.preenche_espiral()
		self.assertEquals( m.matrix, [] )
		
		m = MatrizEspiral(1,1)
		m.preenche_espiral()
		self.assertEquals( m.matrix, [[1]] )
		m.preenche_espiral()
		self.assertEquals( m.matrix, [[1]] )

		m = MatrizEspiral(1,2)
		m.preenche_espiral()
		self.assertEquals( m.matrix, [[1,2]] )
		
		m = MatrizEspiral(2,2)
		m.preenche_espiral()
		self.assertEquals( m.matrix, [[1,2],[4,3]] )
		
		m = MatrizEspiral(3,3)
		m.preenche_espiral()
		self.assertEquals( m.matrix, [[1,2,3],[8,9,4],[7,6,5]] )
		
		m = MatrizEspiral(7,6)
		m.preenche_espiral()
		expected = [[ 1,  2,  3,  4,  5,  6],
					[22, 23, 24, 25, 26,  7],
					[21, 36, 37, 38, 27,  8],
					[20, 35, 42, 39, 28,  9],
					[19, 34, 41, 40, 29, 10],
					[18, 33, 32, 31, 30, 11],
					[17, 16, 15, 14, 13, 12]] 
		self.assertEquals( m.matrix, expected )
		

if __name__ == '__main__':
	unittest.main()