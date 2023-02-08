myfile = open("demo.txt", "r")
myline = myfile.readline()
while myline:
    print(myline, end="")
    myline = myfile.readline()
myfile.close()  