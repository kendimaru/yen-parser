import pytest
from yen_parser import __version__
from yen_parser import parse_yen


def test_version():
    assert __version__ == '0.1.0'


def test_only_numeric():
    assert parse_yen("0") == 0
    assert parse_yen("1") == 1
    assert parse_yen("21") == 21
    assert parse_yen("321") == 321

    assert parse_yen("4321") == 4_321
    assert parse_yen("54321") == 54_321
    assert parse_yen("654321") == 654_321

    assert parse_yen("7654321") == 7_654_321
    assert parse_yen("87654321") == 87_654_321
    assert parse_yen("987654321") == 987_654_321

    assert parse_yen("1987654321") == 1_987_654_321


def test_with_comma():
    assert parse_yen("4,321") == 4_321
    assert parse_yen("54,321") == 54_321
    assert parse_yen("654,321") == 654_321

    assert parse_yen("7,654,321") == 7_654_321
    assert parse_yen("87,654,321") == 87_654_321
    assert parse_yen("987,654,321") == 987_654_321

    assert parse_yen("1,987,654,321") == 1_987_654_321


def test_with_currency_symbol():
    assert parse_yen("¥1") == 1
    assert parse_yen("¥21") == 21
    assert parse_yen("¥321") == 321

    assert parse_yen("¥4321") == 4_321
    assert parse_yen("¥54321") == 54_321
    assert parse_yen("¥654321") == 654_321

    assert parse_yen("¥7654321") == 7_654_321
    assert parse_yen("¥87654321") == 87_654_321
    assert parse_yen("¥987654321") == 987_654_321

    assert parse_yen("¥1987654321") == 1_987_654_321


def test_with_comma_and_currency_symbol():
    assert parse_yen("¥4,321") == 4_321
    assert parse_yen("¥54,321") == 54_321
    assert parse_yen("¥654,321") == 654_321

    assert parse_yen("¥7,654,321") == 7_654_321
    assert parse_yen("¥87,654,321") == 87_654_321
    assert parse_yen("¥987,654,321") == 987_654_321

    assert parse_yen("¥1,987,654,321") == 1_987_654_321


def test_non():
    with pytest.raises(TypeError):
        parse_yen(None)


def test_not_str():
    with pytest.raises(TypeError):
        parse_yen(b'1')

    with pytest.raises(TypeError):
        parse_yen(1)


def test_empty():
    with pytest.raises(ValueError):
        parse_yen("")


def test_blank():
    with pytest.raises(ValueError):
        parse_yen(" ")

    with pytest.raises(ValueError):
        parse_yen("\t")


def test_with_currency_symbol_not_be_ware_of():
    with pytest.raises(ValueError):
        parse_yen("$4,321")


def test_illegal_position_commas():
    with pytest.raises(ValueError):
        parse_yen("43,21")

    with pytest.raises(ValueError):
        parse_yen("5,4321")


def test_illegal_position_currency_symbol():
    with pytest.raises(ValueError):
        parse_yen("4,321¥")


def test_contain_blank_characters():
    with pytest.raises(ValueError):
        parse_yen(" ¥4,321")

    with pytest.raises(ValueError):
        parse_yen("¥4,321 ")

    with pytest.raises(ValueError):
        parse_yen(" 4321")

    with pytest.raises(ValueError):
        parse_yen("4321 ")

    with pytest.raises(ValueError):
        parse_yen("\t4321")


def test_contain_decimal_point_characters():
    with pytest.raises(ValueError):
        parse_yen("1.1")

    with pytest.raises(ValueError):
        parse_yen("4.321")

