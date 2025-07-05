# First Half of Day 1
first_column = []
second_column = []

# Adds each of the .txt lines into a list
with open('./input.txt') as f:
    lines = f.readlines()

# For each item of the list, splits each string by the space and appends the first value and the last into the corresponding list
for line in lines:
    values = line.split(" ")
    first_column.append(int(values[0]))
    second_column.append(int(values[-1].strip("\n")))

first_column = sorted(first_column)
second_column= sorted(second_column)

# With a loop through each index of the lists and substract both index using the absolute value to avoid negatives and then we sum all of them
distance = sum([abs(first_column[index] - second_column[index]) for index in range(len(first_column))])

print(distance)


# Second Half Of Day 1

# Loops through each number of the first column and counts number of occurences in second column multiplied by the number itself, then sums all the list
similarity_score = sum([num*second_column.count(num) for num in first_column])

print(similarity_score)