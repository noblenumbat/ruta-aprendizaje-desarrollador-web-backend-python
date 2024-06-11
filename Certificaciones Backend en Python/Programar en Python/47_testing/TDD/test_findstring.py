from curses.ascii import isdigit
import findstring
import pytest

def test_ispresent():
    assert findstring.ispresent("Bo")

def test_nodigit():
    assert findstring.nodigit("N7")