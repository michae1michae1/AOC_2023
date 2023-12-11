
# Trying to use Regular Expression to solve this one...            
import re


DAY2_DATA = []

# Import as list of strings for each line
with open('AOC_2023\Day2\AOC_DATA_DAY2.txt') as f:
        lines = f.readlines()
        for line in lines:
            DAY2_DATA.append(line.strip())
            
# Define example data as a list of strings
ex_data = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]


# Thresholds for color cases
thresholds = {'red': 12, 'green': 13, 'blue': 14}

# Choose which data to use based on the boolean switch
use_ex_data = False  # Set this to True to use "ex_data", False to use "DAY2_DATA"
data = ex_data if use_ex_data else DAY2_DATA

# Initialize total game points
total_game_points = 0

# Initialize total game power
total_power = 0

# Process each game line
for line in data:
    
    # Split the line into game ID and results
    game_id, results = line.split(':')
    game_id = game_id.strip()
    
    # Calculate game points based on the Game ID
    game_points = int(game_id.split()[1]) if game_id.split()[1].isdigit() else 0
    
    # Initialize dictionary to track maximum numbers for each color in the current game
    max_numbers = {'red': 0, 'green': 0, 'blue': 0}
    
    # Process each result
    pass_result = 'Yes'  # Assume pass until proven otherwise
    for result in results.split(';'):
        # Use re to extract color and number
        matches = re.findall(r'(\d+)\s+(\w+)', result.strip())
        for match in matches:
            number, color = match
            number = int(number)
            
            # Convert color to lowercase
            color_lower = color.lower()
            
            # Check if the color is in the thresholds dictionary
            if color_lower in thresholds:
                
                # Check if the number exceeds the threshold for the specific color
                threshold = thresholds[color_lower]
                
                if number > threshold:
                    pass_result = 'No'
                
                # Update the maximum number for the color in the current game
                max_numbers[color_lower] = max(max_numbers[color_lower], number)
    
    # Set game_points to 0 if pass_result is "No"
    game_points = 0 if pass_result == 'No' else game_points
    
    # Calculate the "Power" for the current game line
    power_result = max_numbers['red'] * max_numbers['green'] * max_numbers['blue']
    
    # Add the game points to the total
    total_game_points += game_points
    
    # Add the power to the total
    total_power += power_result
    
    # Print the original game line with Pass result, game points, max numbers, and Power
    print(f"{game_id}: {results.strip()} -> GP: {game_points} | Max: {max_numbers} -> Power: {power_result}")

# Print the total game points
print(f"\nTotal Game Points: {total_game_points}")

# Print the total game power
print(f"\nTotal Game Points: {total_power}")