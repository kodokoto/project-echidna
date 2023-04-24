import random
import sys 
from enum import Enum

class Socket(Enum):
    EMPTY = 0
    SINGLE = 1
    MULTI = 2

class Pattern:
    def __init__(self, name, sockets, weight=1):
        self.name = name
        self.sockets = sockets
        self.weight = weight
        self.adj_lists = {
            "N": [],
            "E": [],
            "S": [],
            "W": []
        }
    
    def __getitem__(self, key):
        return self.adj_lists[key]
    
    def __setitem__(self, key, value):
        self.adj_lists[key] = value
        self.adj_lists = self.adj_lists
    
    def __repr__(self) -> str:
        return self.name[:3]

    def __str__(self) -> str:
        return self.name[:3]

class Wave:
    def __init__(self, x, y, patterns):
        self.x = x
        self.y = y
        self.patterns = patterns
        self.isCollapsed = False
    
    def collapse(self, pattern=None):
        if self.isCollapsed:
            return 1
        if pattern and pattern not in self.patterns:
            return None
        if pattern:
            self.patterns = [pattern]
            self.isCollapsed = True
            return 1
        
        self.isCollapsed = True
        choice = random.choices(self.patterns, weights=[pattern.weight for pattern in self.patterns])[0]
        while choice.name.split('-')[0] == "dead" and len(self.patterns) > 1:
            choice = random.choices(self.patterns, weights=[pattern.weight for pattern in self.patterns])[0]
        self.patterns = [choice]
        print(f"Collapsed wave at {self.x}, {self.y} to {self.patterns[0]}")
        return 1
    
    @property
    def coords(self):
        return self.x, self.y
    
    @property
    def entropy(self):
        return self.get_entropy()
    
    def get_entropy(self):
        return len(self.patterns)
    
    def get_superposition(self):
        return self.patterns
    
    def has_pattern(self, pattern):
        return pattern in self.patterns
    
    def constrain(self, pattern):
        self.patterns.remove(pattern)
        print(f"removed pattern {pattern} at {self.x}, {self.y} to {self.patterns}")
        if len(self.patterns) == 1:
            self.collapse()

class WaveFunction:
    
    def __init__(self, size, patterns):
        self.size = size
        self.patterns = patterns
        self.waves = [[Wave(x, y, self.patterns.copy()) for y in range(self.size)] for x in range(self.size)]
        self.current_wave = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        
    def get_pattern_by_name(self, name):
        for pattern in self.patterns:
            if pattern.name == name:
                return pattern
        else:
            raise ValueError(f"Pattern with name {name} not found")
    
    def _init_waves(self):
        for x, row in enumerate(self.waves):
            for y, wave in enumerate(row):
                if x == 0 or y == 0 or x == self.size-1 or y == self.size-1:
                    self.collapse_wave(wave, self.get_pattern_by_name("empty"))
                    self.propagate(wave)

    def get_lowest_entropy_wave(self) -> Wave:
        lowest_entropy = float('inf')
        lowest_entropy_waves = []
        for x, row in enumerate(self.waves):
            for y, wave in enumerate(row):
                entropy = wave.entropy
                if entropy <= 1:
                    continue
                if entropy == lowest_entropy:
                    lowest_entropy_waves.append(wave)
                if wave.entropy < lowest_entropy:
                    lowest_entropy = wave.entropy
                    lowest_entropy_waves = [wave]
        return random.choice(lowest_entropy_waves)
    
    def is_fully_collapsed(self):
        for x, row in enumerate(self.waves):
            for y, wave in enumerate(row):
                if not wave.isCollapsed:
                    return False
        return True
    
    def collapse_wave(self, wave: Wave, pattern: Pattern = None):
        return wave.collapse(pattern)
    
    def get_adjacent_waves(self, wave: Wave):
        x, y = wave.coords
        waves = []
        if x > 0:
            waves.append(("W", self.get_wave((x-1, y))))
        if x < self.size-1:
            waves.append(("E",self.get_wave((x+1, y))))
        if y > 0:
            waves.append(("N", self.get_wave((x, y-1))))
        if y < self.size-1:
            waves.append(("S", self.get_wave((x, y+1))))
        return [(direction, wave) for direction, wave in waves if wave is not None]

    def get_wave(self, coords):
        x, y = coords
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return None
        return self.waves[x][y]
        
    def solve(self):
        self._init_waves()
        x = random.randint(1, self.size-2)
        y = random.randint(1, self.size-2)
        while True:
            x = random.randint(1, self.size-2)
            y = random.randint(1, self.size-2)
            res = self.collapse_wave(self.get_wave((x, y)), self.get_pattern_by_name("spawn"))
            if res:
                break
        
        self.remove_spawn_globally((x, y))
        self.iterate(self.get_wave((x, y)))
        while not self.is_fully_collapsed():
            self.iterate()
        self.save_solution()
    
    def save_solution(self):
        with open("map.txt", "w") as f:
            for y in range(self.size):
                for x in range(self.size):
                    f.write(self.get_wave((x, y)).get_superposition()[0].name + ",")
                f.write("\n")
                
    def remove_spawn_globally(self, exclude: tuple[int, int]):
        for x, row in enumerate(self.waves):
            for y, wave in enumerate(row):
                if (x, y) == exclude:
                    continue
                if wave.has_pattern(self.get_pattern_by_name("spawn")):
                    wave.constrain(self.get_pattern_by_name("spawn"))
        
    
    def iterate(self, current_wave: Wave = None):
        if current_wave is None:
            current_wave = self.get_lowest_entropy_wave()
            current_wave.collapse()
        self.propagate(current_wave)

        
    def get_all_possible_neighbours(self, d, superposition: list[Pattern]):
        possible_neighbours = []
        for pattern in superposition:
            for possible_neighbour in pattern[d]:
                possible_neighbours.append(possible_neighbour)
        return possible_neighbours
        
    def propagate(self, wave: Wave):
        stack = [wave]
        while len(stack) > 0:
            current_wave = stack.pop()
            cur_tiles = current_wave.get_superposition()
            
            for d, other_wave in self.get_adjacent_waves(current_wave):
                print(f"propagating {current_wave.get_superposition()} to {other_wave.coords} in direction {d}")
                if other_wave.isCollapsed:
                    continue
                other_tiles = other_wave.get_superposition()[:]
                print(f"other tiles: {other_tiles}")
                possible_neighbours = self.get_all_possible_neighbours(d, cur_tiles)
                print(f"possible neighbours: {possible_neighbours}")
                for tile in other_tiles:
                    print(f'checking if {tile} is in {possible_neighbours}')
                    if tile not in possible_neighbours:
                        other_wave.constrain(tile)
                        if other_tiles not in stack:
                            stack.append(other_wave)
                            
                self.print()
                
    def print(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.get_wave((x, y)).get_superposition(), end=",")
            print()
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
        
def generate_adjacency_lists(patterns):
    for pattern in patterns:
        print(f"generating adjacency lists for {pattern}")
        for direction, sockets in pattern.sockets.items():
            print("generating adjacency list for direction", direction)
            print(f"looking for patterns with sockets {sockets} in direction {opposite_direction(direction)}")
            for other_pattern in patterns:
                print(f"checking {other_pattern}")
                for socket in sockets:
                    if  socket in other_pattern.sockets[opposite_direction(direction)]:
                        print(f"pattern {other_pattern} has socket {socket} in direction {opposite_direction(direction)}")
                        print(f'{other_pattern} already in {pattern.adj_lists[direction]}? : {not other_pattern not in pattern.adj_lists[direction]}')
                        if other_pattern not in pattern.adj_lists[direction]:
                            print(f"adding {other_pattern} to {pattern.adj_lists[direction]}")
                            pattern.adj_lists[direction].append(other_pattern)

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

    stdoutOrigin=sys.stdout 
    sys.stdout = open("log.txt", "w")
    generate_adjacency_lists(patterns)

    for pattern in patterns:
        print(pattern.name)
        for direction, adj_list in pattern.adj_lists.items():
            print(direction, [pattern.name for pattern in adj_list])

    wf = WaveFunction(20, patterns)
    wf.solve()
    
    sys.stdout.close()
    sys.stdout=stdoutOrigin

main()
    