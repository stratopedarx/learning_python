mapping = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def checkio(num):
    if 0 < num <= 10:
        return mapping[num]

    elif 10 < num <= 100:
        decimal = num / 10
        roman_num = decimal * mapping[10] + checkio(num - decimal * 10)
        if roman_num.count(mapping[10]) >= 9:
            roman_num = roman_num.replace(mapping[10] * 9, mapping[10] + mapping[100])
        elif roman_num.count(mapping[10]) >= 5:
            roman_num = roman_num.replace(mapping[10] * 5, mapping[50])
        roman_num = roman_num.replace(mapping[10] * 4, mapping[10] + mapping[50])
        return roman_num


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(4) == 'IV', '4'
    assert checkio(46) == 'XLVI', '46'
    assert checkio(74) == 'LXXIV', '76'
    assert checkio(99) == 'XCIX', '99'
    # assert checkio(499) == 'CDXCIX', '499'
    # assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'