from bank import value


def test_case_insensitivity():
    assert value("HELLO, JOSH") == 0
    assert value("HELLO") == 0
    assert value("hello") == 0

def test_hello():
    assert value("HELLO") == 0
    assert value("hello, world") == 0

def test_phrase():
    assert value("my name is josh") == 100


def main():
    test_phrase()
    test_hello()
    test_case_insensitivity()

if __name__ == "__main__":
    main()
