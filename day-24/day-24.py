# Absolute File Path
with open("/Users/NOHYOONJI/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Relative File Path
with open("../../Desktop/new_file.txt") as f:
    con = f.read()
    print(con)


