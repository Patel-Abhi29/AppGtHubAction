from src.math_operations import add, sub , mul , div

def test_add():
    assert add(2,3) == 5
    assert add(5,5) == 10

def test_sub():
        assert sub(2,3) == -1
        assert sub(5,5) == 0
        assert sub(10,3) == 7
        
def test_mul():
        assert mul(2,3) == 6
        assert mul(5,5) == 25
        assert mul(10,3) == 30

def test_div():
    assert div(3,3) == 1
    assert div(10,5) == 2
