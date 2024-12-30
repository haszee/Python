
def find_connected_sinks(file_path):

	# Read the input file and parse the data
    with open(file_path, 'r',encoding="utf8") as file:
    	lines = file.readlines()

    # clean up the data & add it to a list object
    objects = []
    for line in lines:
        obj, x, y = line.strip().split()
        x, y = int(x), int(y)
        objects.append((obj, x, y))
    
    # Create a grid and populate it with objects
    grid = {}
    sinks = set()
    source = None
    
    for obj, x, y in objects:
        grid[(x, y)] = obj
        if obj == '*':
            source = (x, y)
        elif obj.isalpha():
            sinks.add((x, y))
    
    # Define the possible connections for each pipe type
    # (0,1) means a connection to the right
    # (0,-1) means a connection to the left
    # (-1,0) means a connection upwards
    # (1,0) means a connection downwards
    pipe_connections = {
        '═': [(0, -1), (0, 1)],
        '║': [(-1, 0), (1, 0)],
        '╔': [(0, 1), (1, 0)],
        '╗': [(0, -1), (1, 0)],

        '╚': [(0, 1), (-1, 0)],
        '╝': [(0, -1), (-1, 0)],
        '╠': [(0, 1), (1, 0), (-1, 0)],

        '╣': [(0, -1), (1, 0), (-1, 0)],
        '╦': [(0, -1), (0, 1), (1, 0)],

        '╩': [(0, -1), (0, 1), (-1, 0)]
    }
    
    def get_connections(obj):
        if obj == '*':
            return [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif obj.isalpha():
            return [(-1, 0), (1, 0), (0, -1), (0, 1)]
        else:
            return pipe_connections.get(obj, [])
    
    # Use BFS to find all connected sinks from the source
    from collections import deque
    
    visited = set()
    queue = deque([source])
    connected_sinks = set()
    
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        if (x, y) in sinks:
            connected_sinks.add(grid[(x, y)])
        
        for dx, dy in get_connections(grid[(x, y)]):
            nx, ny = x + dx, y + dy
            if (nx, ny) in grid and (nx, ny) not in visited:
                if (-dx, -dy) in get_connections(grid[(nx, ny)]):
                    queue.append((nx, ny))
    
    # Return the result as a sorted string of sinks
    return ''.join(sorted(connected_sinks))

# Example usage:
# file_path = 'path/to/your/input/file.txt'
print(find_connected_sinks(r"C:\Users\New Owner\Documents\CompSciLearning\coding_qual_input.txt"))
