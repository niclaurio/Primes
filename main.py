import os


from utils import get_execution_times, plot_times

PLOT_FOLDER = "plots"
START = 10**5
STOP = 10**6
INCREMENT = 5 * 10**4
MAX_WORKERS = 8


if __name__ == "__main__":
    os.makedirs(PLOT_FOLDER, exist_ok=True)

    execution_times = get_execution_times(MAX_WORKERS, START, STOP, INCREMENT)

    for oldest_version, newest_version in [
        ("v1", "v2"),
        ("v2", "v3"),
        ("v3", "v4"),
        ("v4", "v5"),
        ("v5", "v6"),
    ]:
        plot_times(
            f"{oldest_version} vs {newest_version}",
            execution_times[oldest_version],
            execution_times[newest_version],
            x_values=range(START, STOP, INCREMENT),
        )
print("ok")
