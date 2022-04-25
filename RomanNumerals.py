class RomanNumerals:
    roman_list = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
                  (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    @staticmethod
    def to_roman(val: int):
        roman_result = ""
        for integer, roman_numeral in RomanNumerals.roman_list:
            while val >= integer:
                val -= integer
                roman_result += roman_numeral
        return roman_result

    @staticmethod
    def from_roman(roman_num: str):
        index, int_result = 0, 0
        for integer, roman_numeral in RomanNumerals.roman_list:
            numeral_part = roman_num[index: index + len(roman_numeral)]
            while numeral_part == roman_numeral:
                int_result += integer
                index += len(roman_numeral)
        return int_result


print(RomanNumerals.to_roman(1998))
print(RomanNumerals.to_roman(3586))
