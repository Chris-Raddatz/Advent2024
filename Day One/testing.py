from collections import Counter

with open("day_one_input.txt", "r") as file:
    lines = file.readlines()
col1, col2 = zip(*(line.strip().split() for line in lines))

col1 = list(col1)
col2 = list(col2)

col1 = [int(item) for item in col1]
col2 = [int(item) for item in col2]

col1 = sorted(col1)
col2 = sorted(col2)

sum = 0

for int1, int2 in zip(col1, col2):
    sum += abs(int1 - int2)
print(sum)


similarity_score = 0

count_dict = dict(Counter(col2))

for num in col1:
    if num in count_dict:
        similarity_score += (num * count_dict[num])
    else:
        continue

print(similarity_score)

