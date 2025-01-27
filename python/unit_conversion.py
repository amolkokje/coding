"""
ref: https://leetcode.com/discuss/interview-question/5923083/Amazon-SDE-2-or-Phone-screen/

{"from": "meters", "to": "feet", "rate": 3.281}
{"from": "feet", "to": "inches", "rate": 12}
{"from": "centimeters", "to": "inches", "rate": 0.3937}
{"from": "meters", "to": "centimeters", "rate": 100}

convert("meters", "inches", 2) → 78.744
"""

conversion_rates = [
    {"from": "meters", "to": "feet", "rate": 3.281},
    {"from": "feet", "to": "inches", "rate": 12},
    {"from": "centimeters", "to": "inches", "rate": 0.3937},
    {"from": "meters", "to": "centimeters", "rate": 100},
]

from collections import deque


def convert(from_unit, to_unit, value, conversion_rates):

    # create a graph of conversion rates
    graph = {}
    for rate in conversion_rates:
        fromu = rate["from"]
        tou = rate["to"]
        rate = rate["rate"]
        if fromu not in graph:
            graph[fromu] = {}
        if tou not in graph:
            graph[tou] = {}
        graph[fromu][tou] = rate
        graph[tou][fromu] = 1.0 / rate

    # perform the conversion
    if from_unit == to_unit:
        return value

    if from_unit not in graph:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in graph:
        raise ValueError(f"Unknown unit: {to_unit}")

    # perform the conversion
    if from_unit in graph and to_unit in graph[from_unit]:
        return value * graph[from_unit][to_unit]
        
    # find the shortest path between the two units
    queue = deque([(1, from_unit)])
    visited = set()

    while len(queue) > 0:
        # print(f"queue = {queue}")
        rate, current_unit = queue.popleft()

        for next_unit in graph[current_unit]:
            if next_unit == to_unit:
                return value * rate * graph[current_unit][next_unit]

            if next_unit not in visited:
                queue.append((rate * graph[current_unit][next_unit], next_unit))
                visited.add(next_unit)


assert convert("meters", "feet", 2, conversion_rates) == 6.562
assert convert("meters", "inches", 2, conversion_rates) == 78.744
