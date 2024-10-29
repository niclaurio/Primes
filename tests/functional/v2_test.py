from primesAlgorithms.v2 import get_primes_lower_n
import pytest


def test_v2():
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
    ]
    result = get_primes_lower_n(102)

    assert len(result) == len(
        expected_result
    ), f"expected {len(expected_result)} primes lower 102 got {len(result)}"

    for el in expected_result:
        assert el in result, f"expected {el} to be prime"

    assert len(get_primes_lower_n(101)) == len(result)

    with pytest.raises(TypeError) as exc_info:
        get_primes_lower_n("foo")
    assert str(exc_info.value) == "Expected n to be a float or int"

    assert get_primes_lower_n(2) == [2]

    assert get_primes_lower_n(-30) == []
