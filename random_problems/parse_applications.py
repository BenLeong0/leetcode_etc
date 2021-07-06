with open("applications.txt", "r") as readfile:
    line = readfile.readline()
    curr = []
    while line:
        if line == "\n":
            print("|".join(curr))
            curr = []
        else:
            if len(curr) == 0:
                curr = line[:-1].split(" - ")
            elif len(curr) == 2:
                date = line[1:11]
                day = date[0:2]
                month = date[3:5]
                year = date[6:]
                curr.append(year + "-" + month + "-" + day)
        line = readfile.readline()