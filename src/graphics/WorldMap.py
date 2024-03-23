from systems.cardinal import get_opposite_direction
from wfc.wfc import Wave, WaveFunction, Pattern, patterns, generate_adjacency_lists
from rooms.Room import Room
from config import debug

class WorldMap:
    
    def __init__(self):
        self.room: Room = self.load_world()
        
        # if debug:
        #     self.display_world_graph()
        
    def current_room(self) -> Room:
        return self.room
    
    def move_to_room(self, room: Room):
        self.room = room
        
    def move_to_room_by_direction(self, direction: str):
        print(f'Moving from {self.room.name}')
        print('in direction', direction)
        print('of')
        print(self.room.adj_rooms)
        print('to', self.room.adj_rooms[direction].name)
        assert direction in self.room.adj_rooms.keys(), f'Invalid direction {direction}'
        self.room = self.room.adj_rooms[direction]
        
    def load_world(self):
        generate_adjacency_lists(patterns)

        for pattern in patterns:
            print(pattern.name)
            for direction, adj_list in pattern.adj_lists.items():
                print(direction, [pattern.name for pattern in adj_list])

        wf = WaveFunction(20, patterns)
        wf.solve()
        wf.save_solution()
        
        return self.load_rooms(wf)
    
    def load_rooms(self, wf: WaveFunction) -> Room:
        # create a graph of rooms from the wave function
        # only load rooms from non-empty waves

        # get the spawn room from the wave function
        spawn_wave = None
        for row in wf.waves:
            for wave in row:
                if wave.patterns[0].name == 'spawn':
                    spawn_wave = wave
                    break
        assert spawn_wave is not None, "Spawn room not found in wave function"
        
        # create stack to hold waves that have been visited
        visited = []
        
        # recursively load rooms, starting with spawn room
        spawn_room = self.load_room(wf, spawn_wave, None, visited)
        
        return spawn_room
    
    
    def load_room(self, wf: WaveFunction, wave: Wave, parent: Wave, visited: list) -> Room:
        # print(f'Loading room {wave.patterns[0].name}')        
        def is_valid(_dir, _wave: Wave):
            
            # print(f'Checking if {_wave.patterns[0].name} is valid')
            
            # check that its in a valid direction 
            if 'empty' in [w.name for w in wave.patterns[0].adj_lists[_dir]]:
                return False
            
            # check if wave is empty
            if _wave.get_superposition()[0].name == 'empty':
                # print(f'{_wave.patterns[0].name} is empty')
                return False
            
            # check if wave has already been visited
            if _wave in visited:
                # print(f'{_wave.patterns[0].name} has already been visited')
                return False
            
            # check if wave is the parent wave
            if _wave == parent:
                # print(f'{_wave.patterns[0].name} is the parent wave')
                return False
            
            # print(f'checking if {_wave.patterns[0].name}')
            print(wave.patterns[0].adj_lists[_dir])
            
            # check that its a valld adjacent wave
            
            if _wave.patterns[0].name not in [w.name for w in wave.patterns[0].adj_lists[_dir]]:
                # print(f'{_wave.patterns[0].name} is not in {wave.patterns[0].adj_lists[_dir]}')
                return False
            
            return True
        
        # add current wave to visited list
        visited.append(wave)
        
        # get all adjacent waves
        adj_waves = wf.get_adjacent_waves(wave)
        
        # remove all empty waves
        # adj_waves[0] is the direction of the wave at adj_waves[1] relative to the current wave
        adj_waves = [wave for wave in adj_waves if is_valid(wave[0], wave[1])]     

        # recursively load adjacent rooms
        adj_rooms = {}        
        for adj_wave in adj_waves:
            # load the adjacent room
            adj_rooms[adj_wave[0]] = self.load_room(wf, adj_wave[1], wave, visited)
            
        # # add parent room to adj_rooms
        # if parent is not None:
        #     adj_rooms[get_opposite_direction(direction)] = parent
        
        # create room 
        room = self.create_room(wave.get_superposition()[0].name, adj_rooms)
        
        # add itself to the adjacency list of all adjacent rooms
        for direction, adj_room in adj_rooms.items():
            adj_room.adj_rooms[get_opposite_direction(direction)] = room
        
        return room
    
    def create_room(self, name, adj_rooms, rotate=0):
        match name:
            case 'spawn':
                from rooms.Spawn import Spawn
                return Spawn(adj_rooms, rotate)
            case 'cross':
                from rooms.Cross import Cross
                return Cross(adj_rooms, rotate)
            case 'straight-ns':
                from rooms.Straight import Straight
                return Straight(adj_rooms, rotate)
            case 'straight-ew':
                from rooms.Straight import Straight
                return Straight(adj_rooms, 1)
            case 'T-nes':
                from rooms.T import T
                return T(adj_rooms, rotate)
            case 'T-esw':
                from rooms.T import T
                return T(adj_rooms, rotate)
            case 'T-swn':
                from rooms.T import T
                return T(adj_rooms, rotate)
            case 'T-wne':
                from rooms.T import T
                return T(adj_rooms, rotate)
            case 'dead-end-n':
                from rooms.DeadEndN import DeadEndN
                return DeadEnd(adj_rooms, rotate)
            case 'dead-end-e':
                from rooms.DeadEndE import DeadEndE
                return DeadEnd(adj_rooms, rotate)
            case 'dead-end-s':
                from rooms.DeadEndS import DeadEndS
                return DeadEnd(adj_rooms, rotate)
            case 'dead-end-w':
                from rooms.DeadEndW import DeadEndW
                return DeadEnd(adj_rooms, rotate)
            case 'corner-ne':
                from rooms.CornerNE import CornerNE
                return DeadEnd(adj_rooms, rotate)
            case 'corner-se':
                from rooms.CornerES import CornerES
                return DeadEnd(adj_rooms, rotate)
            case 'corner-sw':
                from rooms.CornerSW import CornerSW
                return DeadEnd(adj_rooms, rotate)
            case 'corner-nw':
                from rooms.CornerNW import CornerNW
                return DeadEnd(adj_rooms, rotate)
            case default:
                return Room(name, [], adj_rooms, rotate)
    
    def display_world_graph(self):
        # display the graph of rooms using nx and matplotlib
        import networkx as nx
        import matplotlib.pyplot as plt
        
        G = nx.Graph()
        
        # recursively add nodes starting from self.room
        def add_nodes(room: Room):
            G.add_node(room.name)
            for direction, adj_room in room.adj_rooms.items():
                G.add_edge(room.name, adj_room.name)
                G[room.name][adj_room.name]['direction'] = direction
                add_nodes(adj_room)
        
        add_nodes(self.room)
        G.edges(data=True)

        nx.draw(G, with_labels=True)
        plt.show()
        
        return G

        
            
        
                