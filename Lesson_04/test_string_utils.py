import pytest
from string_utils import StringUtils


utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_string, expected', (
    [
        ('cola', 'Cola'),
        ('cOLA', 'COLA'),
        ('hello World', 'Hello World'),
        ('1 cola', '1 Cola'),
        (' hello', ' Hello')
    ]))
def test_capitalize_string_positive(input_string, expected):
    assert utils.capitalize(input_string) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_string, expected', (
    [
        ('f', 'F'),
        ('123', '123'),
        ('', ''),
        (' ', ' '),
        ('.', '.')
    ]))
def test_capitalize_string_negative(input_string, expected):
    assert utils.capitalize(input_string) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_string, expected', (
    [
        (' привет', 'привет'),
        ('  привет', 'привет')
    ]))
def test_trim_positive(input_string, expected):
    assert utils.trim(input_string) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_string, expected', (
    [
        ('привет', 'привет'),
        ('  ', '')
    ]))
def test_trim_negative(input_string, expected):
    assert utils.trim(input_string) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_string, symbol', (
    [
        ('Hello', 'H'),
        ('Hello', 'l'),
        ('123', '2'),
        ('Coca cola', ' '),
        ('Hello, world!', '!')
    ]
))
def test_contains_positive(input_string, symbol):
    assert utils.contains(input_string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize('input_string, symbol', (
    [
        ('Hello', 'h'),
        ('Hello', 'a'),
        ('123', ' '),
    ]
))
def test_contains_negative(input_string, symbol):
    assert utils.contains(input_string, symbol) is False


@pytest.mark.parametrize('input_string, symbol', (
    [
        ('Coca cola', '')
    ]
))
def test_contains_with_empty_symbol(input_string, symbol):
    assert utils.contains(input_string, symbol) is False


@pytest.mark.positive
@pytest.mark.parametrize('input_string, symbol, expected', (
    [
        ('Symbol', 'S', 'ymbol'),
        ('Coca cola', 'o', 'Cca cla'),
        ('Coca cola', 'Coca', ' cola'),
        ('Hello, world', 'wor', 'Hello, ld'),
        ('abc123', '123', 'abc'),
        ('hololo', 'olo', 'hlo')
    ]
))
def test_delete_symbol_positive(input_string, symbol, expected):
    result = utils.delete_symbol(input_string, symbol)
    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_string, symbol, expected', (
    [
        ('Symbol', 's', 'Symbol'),
        ('Hello, world!', 'Helloworld', 'Hello, world!'),
        ('fix.txt', '*', 'fix.txt')
    ]
))
def test_delete_symbol_negative(input_string, symbol, expected):
    result = utils.delete_symbol(input_string, symbol)
    assert result == expected
