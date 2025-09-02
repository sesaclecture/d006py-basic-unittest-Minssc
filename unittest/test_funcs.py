from unit import is_odd, average, mymax, mymin

def test_oddity():
    assert is_odd(1) is True
    assert is_odd(2) is False
    assert is_odd(3) is True
    assert is_odd(42) is False

def test_average():
    assert average([1,2,3]) == 2
    assert average([100, 1000]) == 550
    assert average([999, 999, 999]) == 999 

def test_max():
    assert mymax([1,100,5]) == 100
    assert mymax([1,2,3,4,5,6,7,8,9,10]) == 10
    assert mymax([-100, -10, 0]) == 0

def test_min():
    assert mymin([1,100,5]) == 1
    assert mymin([1,2,3,4,5,6,7,8,9,10]) == 1
    assert mymin([-100, -10, 0]) == -100