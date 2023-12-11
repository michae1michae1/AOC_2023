
#AOC DAY 1
#PART 2 OF 2

AOC_DATA = []

with open('AOC_2023\Day 1\AOC_DATA.txt') as f:
        lines = f.readlines()
        for line in lines:
            AOC_DATA.append(line.strip())


word_to_num = {
    'one': 1, 'two': 2, 'three': 3,
    'four': 4, 'five': 5, 'six': 6,
    'seven': 7, 'eight': 8, 'nine': 9
}

# Create a new dictionary with modified strings
word_to_num_modified = {word: f"{word[0]}{num}{word[-1]}" for word, num in word_to_num.items()}

Ex_data = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrsts6xteen"
]

combos = []

for line in AOC_DATA:
    # Replace words with modified strings
    for word, replacement in word_to_num_modified.items():
        line = line.replace(word, replacement)

    # Find the first and second integers
    Fv = None
    Sv = None
    found_first = False

    for char in line:
        if char.isdigit():
            if not found_first:
                Fv = int(char)
                found_first = True
            else:
                Sv = int(char)
                
    # If Sv is None, set Sv to the same number as Fv
    if Sv is None:
        Sv = Fv
        
    # Calculate Combo and store in a list
    Combo = str(Fv) + (str(Sv) if Sv is not None else "0") if Fv is not None else None
    combos.append(Combo)

    

    # Print the results for each line
    print(f"Original: {line}, Fv: {Fv}, Sv: {Sv}, Combo: {Combo}")

# Calculate and print the total
total = sum(map(int, filter(None, combos)))
print(f"Total: {total}")
