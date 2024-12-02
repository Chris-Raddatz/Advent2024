from collections import Counter

from mkl import second

with open("day_two_input.txt", "r") as file:
    lines = file.readlines()

#### Part 1

result = [list(map(int, entry.strip().split())) for entry in lines]

counted = 0

def is_positive(integer):
    if integer > 0:
        return True
    else:
        return False

for list in result:
    continuous = True
    boolean_list = [True] * (len(list) - 1)
    for i in range(len(list) - 1):
        boolean_list[i] = is_positive(list[i + 1] - list[i])
        difference = abs(list[i + 1] - list[i])
        if difference != 1 and difference != 2 and difference != 3 or difference == 0:
            continuous = False
    if boolean_list == [True] * (len(list) - 1) or boolean_list == [False] * (len(list) - 1):
        pass
    else:
        continuous = False
    if continuous == True:
        counted += 1
print("Safe Reports:", counted)

#### Part 2
## Didn't get to work

second_counted = 0

for list in result:

    n = len(list)
    if n < 2:
        second_counted += 1
        continue

    num_errors = 0
    continuous = True
    boolean_list = [True] * (len(list) - 1)
    for i in range(len(list) - 1):
        boolean_list[i] = is_positive(list[i + 1] - list[i])
        difference = abs(list[i + 1] - list[i])
        if difference != 1 and difference != 2 and difference != 3 or difference == 0:
            num_errors += 1
    if boolean_list == [True] * (len(list) - 1) or boolean_list == [False] * (len(list) - 1):
        continuous = True
    else:
        counted = dict(Counter(boolean_list))
        print(counted)
        for key, counts in counted.items():
            if counts == 1 or counts == len(boolean_list) - 1:
                num_errors += 1
            else:
                num_errors += 1
    if continuous == True and num_errors <= 1:
        second_counted += 1
print("Safe Reports:", second_counted)
#628 was wrong
#553 was wrong







