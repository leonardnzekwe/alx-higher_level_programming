#!/usr/bin/python3
"""
101-lazy_matrix_mul Module
contains the lazy_matrix_mul(m_a, m_b)
a function that multiplies 2 matrices by using the module NumPy
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul
    """
    try:
        """Convert the input matrices to NumPy arrays"""
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        
        """Perform matrix multiplication using np.matmul"""
        result = np.matmul(np_a, np_b)
        
        return result
    except Exception as err:
        raise type(err)(str(err))
