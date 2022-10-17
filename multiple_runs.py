#!/usr/bin/python3

import subprocess
import time


def parse_bench_output(input_text: str) -> float:
    """
    Identify the MFlops output value, which is on the second line
    after the MFLOPS label
    """
    line_with_mflops = -1
    for index, line in enumerate(input_text.split("\n")):
        if "MFLOPS" in line:
            line_with_mflops = index + 2
        if index == line_with_mflops:
            parts = line.split()
            return float(parts[3])
    return -1.0


def run_bench(command: str, iterations: int = 10):
    """
    Store the observed MFlops, and display some stats.
    """
    values = []
    elapsed_seconds = 0.0
    for _ in range(iterations):
        start = time.perf_counter()
        result = subprocess.run(command, capture_output=True, text=True, shell=True).stdout
        elapsed_seconds += time.perf_counter()-start
        values.append(parse_bench_output(result))
    avg = sum(values) / len(values)

    # https://www.geeksforgeeks.org/python-standard-deviation-of-list/
    variance = sum([((x - avg) ** 2) for x in values]) / len(values)
    std_dev = variance ** 0.5

    print("Max: {:.2f}".format(max(values)))
    print("Min: {:.2f}".format(min(values)))
    print("Average: {:.2f}".format(avg))
    print("Std Dev: {:.2f}".format(std_dev))
    print("Seconds: {:.2f}".format(elapsed_seconds))
    print("Runs: {}".format(len(values)))


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: {} <Command> [iterations]".format(sys.argv[0]))
        sys.exit(1)

    if len(sys.argv) == 3:
        try:
            itr = int(sys.argv[2])
            run_bench(sys.argv[1], itr)
        except ValueError:
            run_bench(sys.argv[1])
    else:
        run_bench(sys.argv[1])

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
