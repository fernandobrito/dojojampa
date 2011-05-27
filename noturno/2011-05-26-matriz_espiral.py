# -*- coding: utf-8 -*-
# 2ª Sessão DojoJampa Noturno - 26 de maio de 2011
# http://dojojampa.posterous.com
#
# Problema: http://dojopuzzles.com/problemas/exibe/matriz-espiral/
#
# Status: Incomplento

import unittest

def create_matrix(n_rows, n_columns):
    return [ [ 0 for x in range(n_columns)] for y in range(n_rows) ]

    
def fill_matrix(matrix):
    for i in range(len(matrix[0])):
        matrix[0][i] = i+1
        
    if len(matrix) > 1:
        max_element = len(matrix) * len(matrix[0])
        for i in range(len(matrix[0])):
            matrix[1][i] = max_element
            max_element -= 1
def matrix_3x3(matrix):
    for i in range(len(matrix[0])):
         matrix[0][i] = i+1
         matrix[1]  
    return matrix    

class MyTest(unittest.TestCase):
    def test_create_matrix(self):
        matrix = create_matrix(2, 2)
        expected = [[0, 0], 
                    [0, 0]]
        self.assertEquals(expected, matrix)
        
        matrix = create_matrix(1,1)
        expected = [[0]]
        self.assertEquals(expected, matrix)
        
        matrix = create_matrix(3,2)
        expected = [[0,0],
                    [0,0],
                    [0,0]] 
        self.assertEquals(expected, matrix)
        
        
    def test_matrix(self):
        matrix = create_matrix(1,1)
        filled_matrix = fill_matrix(matrix)
        expected = [[1]]
        self.assertEquals(expected, filled_matrix)
    
    
        matrix = create_matrix(1,2)
        filled_matrix = fill_matrix(matrix)
        expected = [[1, 2]]
        
        self.assertEquals(expected, filled_matrix)
        
        matrix = create_matrix(2,3)
        filled_matrix = fill_matrix(matrix)
        expected = [[1,2,3],[6,5,4]]
        
        self.assertEquals(expected, filled_matrix)
        
        matrix = create_matrix(3,3)
        filled_matrix = fill_matrix(matrix)
        expected = [[1,2,3], [8,9,4], [7,6,5]]
        
        self.assertEquals(expected, filled_matrix)
        
        

if __name__ == '__main__':
    unittest.main()
