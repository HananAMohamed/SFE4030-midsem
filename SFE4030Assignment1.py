class Roman:
    def __init__(self):
        self.map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s):
        convertedNumber = 0
        i = 0
        while i < len(s):
            currentNumber = self.map[s[i]]
            next_num = self.map[s[i + 1]] if i + 1 < len(s) else 0
            if currentNumber >= next_num:
                convertedNumber += currentNumber
            else:
                convertedNumber -= currentNumber
            i += 1
        return convertedNumber

if __name__ == "__main__":
    roman_converter = Roman()
    roman_str = "DCCLXXXVII"
    result = roman_converter.romanToInt(roman_str)
    print("Roman numeral", roman_str, "is equivalent to", result)


def test_roman_to_integer():
    roman_converter = Roman()
    
    # Test cases set
    assert roman_converter.romanToInt("I") == 1
    assert roman_converter.romanToInt("II") == 2
    assert roman_converter.romanToInt("III") == 3
    assert roman_converter.romanToInt("IV") == 4
    assert roman_converter.romanToInt("V") == 5
    assert roman_converter.romanToInt("VI") == 6
    assert roman_converter.romanToInt("VII") == 7
    assert roman_converter.romanToInt("VIII") == 8
    assert roman_converter.romanToInt("IX") == 9
    assert roman_converter.romanToInt("LXXVII") == 77
    assert roman_converter.romanToInt("MMMM") == 4000

if __name__ == "__main__":
    test_roman_to_integer()
    print("success ")
