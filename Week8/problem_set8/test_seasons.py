from seasons import age_in_minutes


def test_age_in_minutes():
    year, month, day = 1999, int("01"), int("01")
    assert age_in_minutes(year, month, day) == 13730400

def main():
    test_age_in_minutes()

main()

if __name__ == "__main__":
    main()