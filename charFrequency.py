file_name = input("what is the name of the file to be examined: ")
pos_ignore = input("Do you want to ignore some characters?: yes or no ")
file_ignored = ""
if(pos_ignore == "yes"):
    file_ignored = input("what is the name of the file with characters to be ignored?: ")

char_dict = {}
ignored_list = []

try:
    with open(file_ignored, "r") as ignored:
        for row in ignored:
            ignored_list.append(row)
        ignored.close()
        for x in range(len(ignored_list)):
            ignored_list[x] = ignored_list[x][0]
except:
    print("ignore characters file not found ")

with open(file_name, "r") as File:
    for row in File:
        for char in row:
            if(char not in ignored_list):
                if(char not in char_dict):
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1
File.close()

max_val = 0
max_key = ' '

for key, value in char_dict.items():
    if (value > max_val):
        max_val = value
        max_key = key
        if(max_key == " "):
            max_key = "space"
print( "The most frequent character was the letter (", max_key,") with ", max_val, "occurences" )

