import pytest

def add(x, y):

    return x + y
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

def test_add_negative():
    assert add(-7, -1) == -8
    
#
#====================================================== 2 passed in 0.04s ======================================================= 
#PS H:\python\python-hyd\pythonlbs> python -m pytest pytest1.py
#===================================================== test session starts ======================================================
#platform win32 -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
#rootdir: H:\python\python-hyd\pythonlbs
#collected 2 items                                                                                                                

#pytest1.py ..                                                                                                             [100%] 

#====================================================== 2 passed in 0.03s ======================================================= 

