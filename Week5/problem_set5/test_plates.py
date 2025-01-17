from plates import is_valid

def test_first_two_letters():
    assert is_valid("AA") == True

def test_ends_with_number():
    assert is_valid("Josh12") == True

def test_no_special_characters():
    assert is_valid("Jo! ._") == False

def test_no_first_two_letters():
    assert is_valid("11Josh") == False

def test_length_check():
    assert is_valid("AB") == True
    assert is_valid("ABCD1") == True
    assert is_valid("ABC") == True
    assert is_valid("ABCDEF11") == False

def test_zero_placement():
    assert is_valid('BLD003') == False

def main():
    test_first_two_letters()
    test_ends_with_number()
    test_no_special_characters()
    test_length_check()
    test_zero_placement()

if __name__ == "__main__":
    main()