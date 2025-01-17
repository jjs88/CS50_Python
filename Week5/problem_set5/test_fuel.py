from fuel import convert, gauge
import pytest



def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/4")

def test_not_an_int():
    with pytest.raises(ValueError):
        convert("cat/5")

def test_gauge_full():
    assert gauge(convert("99/100")) == 'F'

def test_gauge_empty():
    assert gauge(convert("1/100")) == 'E'

def test_gauge_not_empty_or_full():
    assert gauge(convert("50/100")) == "50%"

def main():
    test_divide_by_zero()
    test_x_greater_than_y()
    test_not_an_int()
    test_gauge_full()
    test_gauge_empty()
    test_gauge_not_empty_or_full()

if __name__ == "__main__":
    main()