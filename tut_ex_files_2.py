# Python tutorial ex. 2
# Edit teams.txt so the top line is replaced
# with "This is a new line"

file = open("teams.txt", "r")
outfile = ""
file.close()

# file.readline() ?
file = open("teams.txt", "w")

for i in range(5):
    addline = "This is a new line" + "\n"
    if i == 0:
        file.write(addline)

print ()

file.close()