#Read a Python source file and create another file after removing single-line comments.
file = open("factor.py", "r")
lines = file.readlines()
file.close()
output = open("new_source.py", "w")
for line in lines:
    if not line.strip().startswith("#"):
        output.write(line)
output.close()
print("Comments removed successfully.")