def convert_to_celsius(fahrenheit):
    """(number) -> float
    Return the number of Celsius degrees equivalent to Fahrenheit degrees

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    """

    return (fahrenheit - 32) * 5 / 9

def above_freezing(celsius):
    """ (number) -> bool

    Return True iff temperature celsius degrees is above freezing.

    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """

    return celsius > 0


if __name__ == '__main__':
    fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print('It is above freezing.')
    else:
        print('It is below freezing.')
