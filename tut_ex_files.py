file = open("teams.txt", "w")
file.write ("Manchester United \n")
file.write ("Manchester City \n")
file.write ("Chelsea \n")
file.write ("Burnley \n") 
file.write ("Liverpool \n")
file.close


# reading an displaying 1st and 4th team in the file

file = open ("teams.txt", "r")

for i in range(5):
    line = file.readline()
    if i == 0:
        print(line)
    if i == 3:
        print (line)

file.close()


