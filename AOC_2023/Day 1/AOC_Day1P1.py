
#AOC DAY 1
#PART 1 OF 2

AOC_DATA = []

with open('AOC_2023\Day 1\AOC_DATA.txt') as f:
        lines = f.readlines()
        for line in lines:
            AOC_DATA.append(line.strip())

def translate_and_combine(input_string):
    # Extract numbers from the input string
    numbers = [c for c in input_string if c.isdigit()]

    # Combine the first and last numbers to create a new integer if possible
    if numbers:
        result = int(numbers[0] + numbers[-1])
        return result
    else:
        return 0  # Return 0 when there are no numbers

# Example data:
input_data = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet'
]

# Accumulate the sum of all the results
total_sum = 0

# Apply the function to each line and print the results
for line in AOC_DATA:
    output = translate_and_combine(line)
    total_sum += output
    print(f"Input string: {line}, Result: {output}")

# Print the total sum of all results
print("Total Sum:", total_sum)

