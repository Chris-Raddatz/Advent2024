import numpy as np

with open("day_five_input.txt", "r") as file:
    data = file.readlines()
### Part 1
grids = [x.strip() for x in data]

rules = [x for x in grids if '|' in x]
pages = [x for x in grids if '|' not in x]

pages = pages[1:] #Get rid of empty string

## It would be something like

rules_dict = dict()
for rule in rules:
    print(rule)
    first_num = int(rule.split('|')[0])
    second_num = int(rule.split('|')[1])
    if first_num not in rules_dict:
        rules_dict[first_num] = [second_num]
    else:
        rules_dict[first_num].append(second_num)

print(rules_dict)

## [77, 62, 49, 59, 53]
legible_lists = []
for i in pages:
    nums = [int(num) for num in i.split(",")]
    for idx, num in enumerate(nums):
        if idx == len(nums) - 1:  # Have to remove 2 because of last number if statement
            legible_lists.append(nums)
            break
        rest_of_nums = nums[idx + 1:]
        check_nums = rules_dict[num]
        if all(number in check_nums for number in rest_of_nums):
            if idx == len(nums) - 1: #Have to remove 2 because of last number if statement
                legible_lists.append(nums)
        else:
            break

median_num_sum = 0
for i in legible_lists:
    n = len(i)
    median = i[n // 2]
    median_num_sum += median
print("Median Sums: ", median_num_sum)