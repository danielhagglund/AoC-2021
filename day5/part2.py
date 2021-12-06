def create_coordinate(item):
    line_end_points = item.split(' -> ')
    start_point = line_end_points[0].split(',')
    end_point = line_end_points[1].split(',')
    start_coordinate = {'x': int(start_point[0]), 'y': int(start_point[1])}
    end_coordinate = {'x': int(end_point[0]), 'y': int(end_point[1])}
    return [start_coordinate, end_coordinate]

def extract_horizontal_lines(coords):
    horizontal_lines = []
    for item in coords:
        if item[0]['x'] == item[1]['x']:
            horizontal_lines.append(item)
    return horizontal_lines

def extract_vertical_lines(coords):
    vertical_lines = []
    for item in coords:
        if item[0]['y'] == item[1]['y']:
            vertical_lines.append(item)
    return vertical_lines 

def extract_diagonal_lines(coords):
    diagonal_lines = []
    for item in coords:
        if (item[0]['y'] != item[1]['y']) and (item[0]['x'] != item[1]['x']):
            diagonal_lines.append(item)
    return diagonal_lines

def create_grid():
    grid_size = 1000
    grid = []
    line = 0
    while line < grid_size:
        pos = 0
        row = []
        while pos < grid_size:
            row.append({'x': pos, 'y': line, 'count': 0})
            pos = pos + 1
        grid.append(row)
        line = line +1
    return grid     
            
def print_grid(grid):
    for row in grid:
        curr_row = ''.join([str(item['count']) for item in row])
        print(curr_row)

def add_horizontal_lines_to_grid(grid, lines):
    for coords in lines:
        y1 = coords[0]['y']
        y2 = coords[1]['y']
        miny = 0
        maxy = 0
        if y1 > y2:
            miny = y2
            maxy = y1
        if y1 < y2:
            miny = y1
            maxy = y2
        ypos = miny
        while ypos <= maxy:
            grid[ypos][coords[0]['x']]['count'] = grid[ypos][coords[0]['x']]['count'] + 1
            ypos = ypos + 1

def add_vertical_lines_to_grid(grid, lines):
    for coords in lines:
        x1 = coords[0]['x']
        x2 = coords[1]['x']
        minx = 0
        maxx = 0
        if x1 > x2:
            minx = x2
            maxx = x1
        if x1 < x2:
            minx = x1
            maxx = x2
        xpos = minx
        while xpos <= maxx:
            grid[coords[0]['y']][xpos]['count'] = grid[coords[0]['y']][xpos]['count'] + 1
            xpos = xpos + 1

def add_diagonal_lines(grid, lines):
    for coords in lines:
        x1 = coords[0]['x']
        x2 = coords[1]['x']
        y1 = coords[0]['y']
        y2 = coords[1]['y']
        if x1 > x2:
            stepx = -1
        if x1 < x2:
            stepx = 1
        if y1 > y2:
            stepy = -1
        if y1 < y2:
            stepy = 1
        xpos = x1
        ypos = y1
        times = abs(x1-x2)
        while times >= 0:
            grid[ypos][xpos]['count'] = grid[ypos][xpos]['count'] + 1
            if stepx == -1:
                xpos = xpos - 1
            else:
                xpos = xpos + 1
            if stepy == -1:
                ypos = ypos - 1
            else:
                ypos = ypos + 1
            times = times - 1 

def count_overlap_points(grid):
    overlaps = 0
    for line in grid:
        for coord in line:
            if coord['count'] > 1:
                overlaps = overlaps + 1
    return overlaps

# Read lines from input
input_data = open("./line_input.txt").read().splitlines()

coordinates = []

for item in input_data:
    coordinates.append(create_coordinate(item))

# Find all horizontal and vertical lines
horizonatal_lines = []
vertical_lines = []
horizontal_lines = extract_horizontal_lines(coordinates)
vertical_lines = extract_vertical_lines(coordinates)
diagonal_lines = extract_diagonal_lines(coordinates)

grid = []
grid = create_grid()

add_horizontal_lines_to_grid(grid, horizontal_lines)
add_vertical_lines_to_grid(grid, vertical_lines)
add_diagonal_lines(grid, diagonal_lines)

overlap_count = count_overlap_points(grid)

print(overlap_count)

