
#AOC DAY 1
#PART 1 OF 2

# any number adjacent to a symbol, even diagonally, is a "part number" 
# and should be included in your sum. (Periods (.) do not count as a symbol.)


DAY3_DATA = []

# Import as list of strings for each line
with open('AOC_2023\Day3\DAY3_DATA.txt') as f:
        lines = f.readlines()
        for line in lines:
            DAY3_DATA.append(line.strip())
            
ex_data = [
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

use_ex_data = True  # Set this to True to use "ex_data", False to use "DAY3_DATA"
data = ex_data if use_ex_data else DAY3_DATA

class Schematic:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
        self.part_numbers = {}
        self.stored_indexes = set()
        self.results_array = []

    def set_part_numbers(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] not in ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    id_match = []

                    for dir_i, dir_j in directions:
                        new_i, new_j = i + dir_i, j + dir_j

                        if 0 <= new_i < self.rows and 0 <= new_j < self.cols:
                            id_match.append((new_i, new_j))
                            self.stored_indexes.add((new_i, new_j))
                        else:
                            id_match.append(None)  # Adding None for positions outside the schematic

                    self.part_numbers[(i, j)] = tuple(id_match)

    def report_positions(self):
        for position, id_match in self.part_numbers.items():
            print(f"Symbol at Pos {position}, Surrounding Index: {id_match}")
        print(f"\nGiven Position (i, j), Surrounding Pos:  ['R', 'D', 'L', 'U','TR','BL','BR','TL']\n")

    def show_surrounding_characters(self):
        for position, id_match in self.part_numbers.items():
            characters = self.get_surrounding_characters(position)
            print(f"Characters in the Surrounding Positions: {characters}")

    def get_surrounding_characters(self, position):
        characters = []
        for dir_i, dir_j in self.part_numbers[position]:
            if dir_i is not None and dir_j is not None:
                characters.append(self.data[dir_i][dir_j])
        return characters

    def check_positions_in_line(self, line_number):
        line_numbers = []  # Create a list to store grouped numbers for the line
        for j in range(self.cols):
            position = (line_number, j)
            result = "no"

            # Check if the position is in the stored indexes
            if position in self.stored_indexes:
                # Check if the character at the position is a number
                if self.data[position[0]][position[1]].isdigit():
                    # Check if the number has a neighbor to the left
                    if j > 0 and self.data[position[0]][j - 1].isdigit():
                        result = self.data[position[0]][position[1]]
                    # Check if the number has a neighbor to the right
                    elif j < self.cols - 1 and self.data[position[0]][j + 1].isdigit():
                        result = self.data[position[0]][position[1]]

            line_numbers.append(result)  # Append the result to the line_numbers list

        # Print the line numbers only once for the entire line
        if any(line_numbers):
            print(f"Line {line_number}: {', '.join(line_numbers)}")

    def check_positions_in_all_lines(self):
        for i in range(self.rows):
            self.check_positions_in_line(i)
            
    def get_full_string_from_position(self, position):
        if position in self.stored_indexes:
            i, j = position
            initial_char = self.data[i][j]

            # Check if the initial character is a digit
            if not initial_char.isdigit():
                return None

            build_string = initial_char

            # Check nearby neighbors on the left
            left_j = j - 1
            while left_j >= 0 and self.data[i][left_j].isdigit():
                build_string = self.data[i][left_j] + build_string
                left_j -= 1

            # Check nearby neighbors on the right
            right_j = j + 1
            while right_j < self.cols and self.data[i][right_j].isdigit():
                build_string += self.data[i][right_j]
                right_j += 1

            full_string = build_string
            return full_string
        else:
            return None

    def find_grouped_numbers(self):
        total_sum = 0  # Initialize total sum
        for i in range(self.rows):
            line_sums = set()  # Create a set to store the sums of integers for the line
            for j in range(self.cols):
                position = (i, j)
                grouped_numbers = self.get_full_string_from_position(position)
                if grouped_numbers is not None:
                    grouped_numbers_int = int(grouped_numbers)
                    line_sums.add(grouped_numbers_int)

            # Print the sum of integers on the current line
            if line_sums:
                print(f"Line {i}: {', '.join(map(str, line_sums))}")

            # Add the sum of integers on the current line to the total
            total_sum += sum(line_sums)

        # Print the total sum across all lines
        print(f"\nTotal Sum Across All Lines: {total_sum}")

            
# Example usage with the chosen data source
schematic = Schematic(data)
schematic.set_part_numbers()
schematic.report_positions()
schematic.show_surrounding_characters()

print('')

# Example usage to check positions in all lines and print the results array
schematic.check_positions_in_all_lines()

print('')

#Show full string numbers for each line
schematic.find_grouped_numbers()