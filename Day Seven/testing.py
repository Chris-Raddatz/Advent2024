from itertools import product

with open("day_seven_input.txt", "r") as file:
    data = file.readlines()

lines = [x.strip() for x in data]

def permutations(checking_num, nums):
    number_of_numbers = len(nums)
    operations = product(['+', '*'], repeat=number_of_numbers - 1)
    for equation in operations:
        result = nums[0]
        for i in range(number_of_numbers - 1):
            if equation[i] == "+":
                result += nums[i + 1]
            else:
                result *= nums[i + 1]
        if result == checking_num:
            return result
    return 0

equals = [int(x.split(":")[0]) for x in lines]
right_side = [x.split(":")[1].strip() for x in lines]
count = 0
for list, checked in zip(right_side, equals):
    nums = [int(x) for x in list.split(" ")]
    count += int(permutations(checked, nums))
print("Total Count:", count)
