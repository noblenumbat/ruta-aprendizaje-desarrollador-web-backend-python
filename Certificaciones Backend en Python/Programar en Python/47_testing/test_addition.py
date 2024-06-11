import addition
import pytest 

def test_add():
    # assert False # el test falla independientemente del código
    assert addition.add(4, 5) == 9 

def test_sub():
    assert addition.sub(4, 5) == -1
    # pass # la prueba se supera independientemente de cualquier error