fileName = input("How is your file called: ")
while(True):
    line = "{"
    inputText = input("What do you want to do(1=read the file, 2=write in the file, 3=create the file, exit=exit): ")
    if (inputText == "1"):
        file = open(fileName,"r")
        print(file.read())
        file.close()

    if (inputText == "2"):
        con = "y"
        content = ""
        name = ""
        value = ""
        file = open(fileName, "r")
        line = file.read().replace("}",",")
        file = open(fileName,"w")
        # if (file):
        #     line = ""
        #     content = file.read().replace("}", ",")
        #     file.close()
        #     file = open(fileName,"w")
        #     file.write(content)
        while (con == "y"):

            name = input("Whats the name of the propertie: ")
            value = input("Whats the value of the propertie:?")
            line =f"{line} \"{name}\" : \"{value}\""
            con = input("Do you want to continue(y/n): ")
            if (con == "y"):
                line = line + ","
        line = line + "}"
        file.write(line)
        file.close()

    if (inputText == "3"):
        file = open(fileName, "w")
        line = "{"
        file.write(line)
        file.close()

    if (inputText == "exit"):
        break
