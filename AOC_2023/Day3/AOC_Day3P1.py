
#AOC DAY 3
#PART 1 OF 2

# any number adjacent to a symbol, even diagonally, is a "part number" 
# and should be included in your sum. (Periods (.) do not count as a symbol.)

         
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

# representing position in grid with coordinates
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

# grid as dictionary - Key is Position
Grid = dict[Position, str]

# Convert / Parse our input data into a grid
def lines_to_grid(lines: list[str]) -> Grid:
    grid: Grid = {}

    # Assign x for characters (cols), y for lines (rows)
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            grid[Position(x, y)] = character

    return grid


n_directions: list[Position] = [
    Position(dx, dy)
    
    for dx in [-1, 0, 1]
    for dy in [-1, 0, 1]
    
    # handle the fact that 0 and 0 change in direction would be the current position, we don't want that
    if not (dx == 0 and dy == 0)
]

def get_neighbours(position: Position, grid: Grid) -> set[Position]:
    return {
        
        # now we can navigate the grid using our classes
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

        # we want to get the value of this and also the positions
        length = find_length_of_number(line, starting_position=x)
        value = int(line[x:x + length])
        positions = {Position(x + i, line_number) for i in range(length)}
        
        # Important because we need to know all of the positions for the entire new number so we do not have duplicates
        new_number = NumberWithPosition(value, positions)
        numbers.append(new_number)

        x += length
  
    return numbers

def find_length_of_number(line, starting_position):
    length = 1
    while starting_position + length < len(line):
        next_character = line[starting_position + length]
        if next_character.isdigit():
            length += 1
        else:
            break

    return length

def solve(lines: list[str]) -> int:
    numbers = find_numbers_in_lines(lines)
    grid = lines_to_grid(lines)

    Part_numbers = 0
    
    for number in numbers:
        if has_adjacent_symbol(grid, number):
            Part_numbers += number.value
            
        print(f'PART NUM: {number.value}')
        
    return Part_numbers

def has_adjacent_symbol(grid: Grid, number: NumberWithPosition) -> bool:
    
    neighbours = get_neighbours_of_set(number.positions, grid)
    
    # check in the grid if the neighbar position in the neighbors set is a symbol
    for neighbour in neighbours:
        if is_symbol(grid[neighbour]):
            return True

    return False

def is_symbol(character: str) -> bool:
    if character.isdigit() or character == ".":
        return False

    return True

def WIN():
    lines = read_input()
    solution = solve(lines)
    print(f"\n{solution = }\n")

WIN()

    
