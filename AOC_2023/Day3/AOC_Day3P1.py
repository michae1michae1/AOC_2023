
#AOC DAY 3
#PART 2 OF 2

# Find 2 numbers adjacent to a star symbol
# If exactly 2 match, multiply them together to get gear ratio, then sum those values
         
# Import as list of strings for each line
def read_input(use_example_data: bool = False) -> list[str]:
    if use_example_data:
        return [
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..'
        ]
    else:
        with open("AOC_2023/Day3/DAY3_DATA.txt") as f:
            lines = f.read().splitlines()
        return lines

# Create class representing position in grid with coordinates
class Position:
    
    # Setup methods to do operations with these position coords
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

# Represent grid as dictionary - Key is Position
Grid = dict[Position, str]

# Convert / Parse our input data into a grid
def lines_to_grid(lines: list[str]) -> Grid:
    grid: Grid = {}

    # Assign x for characters (cols), y for lines (rows)
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            grid[Position(x, y)] = character

    return grid

# Directions for finding the symbol neighbors
n_directions: list[Position] = [
    Position(dx, dy)
    # change in x and y in all of these combinations
    for dx in [-1, 0, 1]
    for dy in [-1, 0, 1]
    # handle the fact that 0 and 0 change in direction would be the current position, we don't want that
    if not (dx == 0 and dy == 0)
]

# Set perameters for getting our neighbors
def get_neighbours(position: Position, grid: Grid) -> set[Position]:
    return {
        
        #So now we can navigate the grid using our classes
        position + direction
        for direction in n_directions
        
        # check if is within the grid
        if position + direction in grid.keys()
    }

# Use previous function to get all nneighbors of our set of positions in the grid
def get_neighbours_of_set(positions: set[Position],
                          grid: Grid,
                          ) -> set[Position]:
    neighbours = set()
    
    # use position, to find all positions in set
    for position in positions:
        
        # local will be for each position in grid
        local_neighbours = get_neighbours(position, grid)
        
        # update the set so it now contains both neighbors and local
        neighbours.update(local_neighbours)
    
    # handles filtering out the positions themselves, returns only real neighbors
    # similar to the if not (dx == 0 and dy == 0) function above
    return neighbours - positions

# This is what saves the numbers for the string parse, ex. 3digit num at 3 positions
# This is a better way to check for the entire number instead of each digit at a time
class NumberWithPosition:
    def __init__(self, value: int, positions: set[Position]):
        self.value = value
        self.positions = positions

# Need to parse the NumberWithPosition out of the set of input lines
# collect all the numbers we need in one list
def find_numbers_in_lines(lines: list[str]) -> list[NumberWithPosition]:
    numbers: list[NumberWithPosition] = []

    for y, line in enumerate(lines):
        numbers.extend(find_numbers_in_line(line, line_number=y))

    return numbers

# How we pull the numbers out of the line
def find_numbers_in_line(line: str, line_number: int):
    # "467..114.."
    numbers: list[NumberWithPosition] = []
    
    # Could use re, but in this case we code out the logic to find 
    x = 0
    while x < len(line):
        
        # if not a digit then ignore, we basically just pulling all digits
        if not line[x].isdigit():
            x += 1
            continue

        # if it is digit, then we want to get the value of this and also the positions
        length = find_length_of_number(line, starting_position=x)
        value = int(line[x:x + length])
        positions = {Position(x + i, line_number) for i in range(length)}
        
        # So now we have a number that stores both the value and the positions
        # Important because we need to know all of the positions for the entire new number so we do not have duplicates
        new_number = NumberWithPosition(value, positions)
        numbers.append(new_number)

        x += length
  
    return numbers

# Use to detemine number of digits in a number
def find_length_of_number(line, starting_position):
    length = 1
    while starting_position + length < len(line):
        next_character = line[starting_position + length]
        if next_character.isdigit():
            length += 1
        else:
            break

    return length

# Solver using final functions
def solve(lines: list[str]) -> int:
    numbers = find_numbers_in_lines(lines)
    grid = lines_to_grid(lines)

    Part_numbers = 0
    
    for number in numbers:
        if has_adjacent_symbol(grid, number):
            Part_numbers += number.value
            
        print(f'PART NUM: {number.value}')
        
    return Part_numbers

# checking if a number is adjacent to symbol
def has_adjacent_symbol(grid: Grid, number: NumberWithPosition) -> bool:
    
    # first we go grab all the neighbors of the set
    neighbours = get_neighbours_of_set(number.positions, grid)
    # then we check in the grid if the neighbar position in the neighbors set is a symbol
    for neighbour in neighbours:
        if is_symbol(grid[neighbour]):
            return True

    return False

# ID a symbol
def is_symbol(character: str) -> bool:
    if character.isdigit() or character == ".":
        return False

    return True

# Final
def WIN():
    lines = read_input()
    solution = solve(lines)
    print(f"\n{solution = }\n")

WIN()

    
