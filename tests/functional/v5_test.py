import pytest

from primesAlgorithms.v5 import get_primes_lower_n


def test_v5():
    expected_result = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
    ]

    result = get_primes_lower_n(113)

    assert len(expected_result) == len(
        result
    ), f"expected {len(expected_result)} primes got {len(result)}"

    for el in expected_result:
        assert el in result, f"expected {el} to be a prime number"

    assert expected_result == get_primes_lower_n(114)
    assert expected_result == get_primes_lower_n(121)

    assert expected_result == get_primes_lower_n(122)

    with pytest.raises(TypeError) as exc_info:
        get_primes_lower_n("foo")
    assert str(exc_info.value) == "Expected n to be a float or int"

    assert get_primes_lower_n(2) == [2]

    assert get_primes_lower_n(-30) == []
