import re

with open("day_three_input.txt", "r") as file:
    data = file.read()
### Part 1
pattern = r'mul(\(\d+,\d+\))' #Initial Pattern

# Find all matches in the text
matches = re.findall(pattern, data) #Find matches and insert into list
final_result = 0 #Initialize variable

new_pattern = r'\((\d+),(\d+)\)' #Search pattern for our number
for match in matches:
    new_matches = re.search(new_pattern, match)
    first_num = new_matches.group(1) #First number
    second_num = new_matches.group(2) #Second number
    final_result += int(first_num) * int(second_num) #Add in our new number
print("First Part Final Result: ", final_result)

#### Second Part

second_part_result = 0

pattern = r'mul\(\d+,\d+\)|\bdo\(\)|\bdon\'t\(\)' #Add new options for do() or don't()

matches = re.findall(pattern, data) #again search and list

multiply = True #Initialize True
for i in matches:
    if i == "do()": #If do() change to True
        multiply = True
        continue
    elif i == "don't()": #If don't() change to False
        multiply = False
        continue
    else:
        if multiply: #If multiply is true we do the same as before
            new_matches = re.search(new_pattern, i)
            first_num = new_matches.group(1)
            second_num = new_matches.group(2)
            second_part_result += int(first_num) * int(second_num)
        else: #Otherwise keep going
            continue

print("Second Part Final Result: ", second_part_result)










