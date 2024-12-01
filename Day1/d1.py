from collections import Counter

with open('d1data.txt', 'r') as file:
    # Formats ints with every line, Tuples them together.
    data_list = [tuple(map(int, line.split())) for line in file]
# Sorts the first and second pairs 
first_column = sorted(pair[0] for pair in data_list) 
second_column = sorted(pair[1] for pair in data_list) 
# Zips the tupples into a sort
sorted_tuples = list(zip(first_column, second_column))
# Does the math, Subtract the pairs -> ABS them -> Sum
out_tuple = [(abs(pair[0] - pair[1])) for pair in sorted_tuples]
total = sum(out_tuple)
# Print
print("Part 1:", total)

# Part 2; Similarity
# Count the similars in the second column
similar = Counter(second_column)
# Lookup the amount of time first collumn nums appear in second colum, done in previous step.
lookup = [(num, similar.get(num, 0)) for num in first_column]
# Do da math
simscores = [(pair[0] * pair[1]) for pair in lookup]
simsum = sum(simscores)
# Print
print("Part 2:", simsum)