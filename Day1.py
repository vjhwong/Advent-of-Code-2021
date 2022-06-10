aoc_day1_file = "AoC/AoC_inputs/aocday1.txt"

with open(aoc_day1_file) as f:
    f_contents = [int(i) for i in f.readlines()]  # Convert textfile to list of integers

# Part 1
counter = 0
for i in range(len(f_contents) - 1):
    # Add to counter if the current value is less than the next one
    if f_contents[i] < f_contents[i + 1]:
        counter += 1
print(counter)

# Part 2
slider_counter = 0
for i in range(1, len(f_contents) - 1):
    # Add to counter if the current sum is less than the next one
    if sum(f_contents[i - 1 : i + 2]) < sum(f_contents[i : i + 3]):
        slider_counter += 1
print(slider_counter)
