#!/usr/bin/python3
"""
100-matrix_mul module
That contains matrix_mul(m_a, m_b) function
a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul function
    """
    if m_a is None or type(m_a) != list:
        raise TypeError("m_a must be a list")
    if m_b is None or type(m_b) != list:
        raise TypeError("m_b must be a list")
    if any(type(row) != list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(row) != list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if (
        any(type(item) != int for row in m_a for item in row) and
        any(type(item) != float for row in m_a for item in row)
    ):
        raise TypeError("m_a should contain only integers or floats")
    if (
        any(type(item) != int for row in m_b for item in row) and
        any(type(item) != float for row in m_b for item in row)
    ):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(m_a[0]) != len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(m_b[0]) != len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for column in m_a:
        new_list = []
        for i in range(len(m_b[0])):
            j = 0
            cell = 0
            for row in m_b:
                cell += column[j] * row[i]
                j += 1
            new_list.append(cell)
        new_matrix.append(new_list)

    return new_matrix
