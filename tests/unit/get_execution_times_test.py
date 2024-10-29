from utils import get_execution_times


def side_effect_func(n, func):
    execution_times = {
        "v1": 0.1,
        "v2": 0.2,
        "v3": 0.15,
        "v4": 0.25,
        "v5": 0.05,
        "v6": 0.3,
    }

    func_version = func.__module__.split(".")[-1]
    return execution_times[f"{func_version}"]


def test_get_execution_times(mocker):
    mock_get_time = mocker.patch("utils.get_function_execution_time")
    mock_get_time.side_effect = side_effect_func

    results = get_execution_times(max_workers=2, start=10, stop=20, increment=5)

    assert len(results) == 6

    assert results["v1"] == [0.1, 0.1]

    assert results["v2"] == [0.2, 0.2]

    assert results["v3"] == [0.15, 0.15]

    assert results["v4"] == [0.25, 0.25]

    assert results["v5"] == [0.05, 0.05]

    assert results["v6"] == [0.3, 0.3]
