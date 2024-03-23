import random
import sys
from enum import Enum
from typing import Dict, List, Tuple

class Socket(Enum):
    EMPTY = 0
    SINGLE = 1
    MULTI = 2

class Pattern:
    def __init__(self, name, sockets, weight=1):
        self.name = name
        self.sockets = sockets
        self.weight = weight
        self.adj_list = {}

    def __repr__(self) -> str:
        return self.name[:3]

    def __str__(self) -> str:
        return self.name[:3]

class Wave:
    def __init__(self, pattern: Pattern):
        self.pattern = pattern
        self.adj_list = {}

class WaveFunction:
    def __init__(self, patterns: List[Pattern]):
        self.patterns = patterns
        self.waves = []
        self.current_wave = None

    def _get_pattern_by_name(self, name: str) -> Pattern:
        for pattern in self.patterns:
            if pattern.name == name:
                return pattern
        else:
            raise ValueError(f"Pattern with name {name} not found")

    def _get_adj_wave(self, wave: Wave, direction: str) -> Wave:
        if direction in wave.adj_list:
            return wave.adj_list[direction]
        return None

    def _collapse_wave(self, wave: Wave):
        wave.pattern = random.choices(self.patterns, weights=[pattern.weight for pattern in self.patterns])[0]
        return wave

    def _get_lowest_entropy_wave(self) -> Wave:
        lowest_entropy = float('inf')
        lowest_entropy_waves = []
        for wave in self.waves:
            entropy = len(wave.patterns)
            if entropy <= 1:
                continue
            if entropy == lowest_entropy:
                lowest_entropy_waves.append(wave)
            if entropy < lowest_entropy:
                lowest_entropy = entropy
                lowest_entropy_waves = [wave]
        return random.choice(lowest_entropy_waves)

    def _propagate(self, wave: Wave):
        directions = {
            "N": (0, -1),
            "E": (1, 0),
            "S": (0, 1),
            "W": (-1, 0)
        }
        for direction, sockets in wave.pattern.sockets.items():
            dx, dy = directions[direction]
            adj_wave = self._get_adj_wave(wave, direction)
            if adj_wave:
                adj_pattern = adj_wave.pattern
                for socket in sockets:
                    if socket in adj_pattern.sockets[opposite_direction(direction)]:
                        if adj_wave not in wave.adj_list.values():
                            wave.adj_list[direction] = adj_wave
                            adj_wave.adj_list[opposite_direction(direction)] = wave

    def solve(self, num_waves):
        self.current_wave = Wave(self._get_pattern_by_name("spawn"))
        self.waves.append(self.current_wave)
        while len(self.waves) < num_waves:
            self.current_wave = self._collapse_wave(self.current_wave)
            self._propagate(self.current_wave)
            self.waves.append(self.current_wave)
        
    def save_solution(self):
        with open("graph.txt", "w") as f:
            for wave in self.waves:
                f.write(wave.pattern.name + ",")
            f.write("\n")


    def print_solution(self):
        for wave in self.waves:
            print(wave.pattern.name, end=",")
        print()

def opposite_direction(direction):
    if direction == "N":
        return "S"
    if direction == "S":
        return "N"
    if direction == "E":
        return "W"
    if direction == "W":
        return "E"

patterns = [
    Pattern(
        "empty",
        {
            "N": [0],
            "E": [0],
            "S": [0],
            "W": [0]
        }
    ),
    Pattern(
        "spawn", 
        {
            "N": [2],
            "E": [0],
            "S": [0],
            "W": [0]
        }
    ),
    Pattern(
        "dead-end-s",
        {
            "N": [0],
            "E": [0],
            "S": [1],
            "W": [0]
        }
    ),
    Pattern(
        "dead-end-e",
        {
            "N": [0],
            "E": [1],
            "S": [0],
            "W": [0]
        }
    ),
    Pattern(
        "dead-end-n",
        {
            "N": [1],
            "E": [0],
            "S": [0],
            "W": [0]
        }
    ),
    Pattern(
        "dead-end-w",
        {
            "N": [0],
            "E": [0],
            "S": [0],
            "W": [1]
        }
    ),
    Pattern(
        "straight",
        {
            "N": [2],
            "E": [0],
            "S": [2],
            "W": [0]
        }
    ),
    Pattern(
        "corner",
        {
            "N": [2],
            "E": [0],
            "S": [0],
            "W": [2]
        }
    ),
    Pattern(
        "T",
        {
            "N": [2, 1],
            "E": [2, 1],
            "S": [2, 1],
            "W": [0]
        },
    ),
    Pattern(
        "cross",
        {
            "N": [2, 1],
            "E": [2, 1],
            "S": [2, 1],
            "W": [2, 1]
        },
        0.5
    )
]

def main():
    stdout_origin = sys.stdout
    sys.stdout = open("log.txt", "w")

    wf = WaveFunction(patterns)
    wf.solve(100)
    wf.save_solution()

    sys.stdout.close()
    sys.stdout = stdout_origin

if __name__ == "__main__":
    main()
