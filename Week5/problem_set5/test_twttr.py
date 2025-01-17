from twttr import shorten

def main():
    test_puncuation()
    test_capitalized_vowel_replacement()
    test_numbers()


def test_puncuation():
    assert shorten("My name's. is!") ==  "My nm's. s!"

def test_capitalized_vowel_replacement():
    assert shorten("JOSH") == "JSH"

def test_numbers():
    assert shorten("Josh123") == "Jsh123"



if __name__ == "__main__":
    main()
