import os, termcolor

global dataArr, activeFile, fileName
dataArr = None
activeFile = False
fileName = ""
nL = "\n"

def getArray():
    while True:
        try:
            global fileName
            fileName = str(input("Please enter the path of the file: "))
            with open(f"{'testData/' * (not ('/' in fileName))}{fileName}.txt", "r") as doc:
                txt = doc.read()
                txt = txt.replace("\n", "")
                array = txt.split(",")
                doc.close()
            break
        except:
            os.system('cls')
            print("Not a valid file\n")

    for i in range(int(len(array) / 5)):
        temp = [str(array[i]), str(array[i + 1]), int(array[i + 2]), int(array[i + 3]), float(array[i + 4][:-1])]
        for _j in range(4):
            array.pop(i)
        array[i] = temp
    array = sorted(array, key = lambda x: x[0], reverse = False)

    for i in range(len(array)):
        alert = (array[i][3] % 90 >= 83) or (array[i][3] % 90 == 0)
        array[i].append((termcolor.colored("Service Soon", "red") * alert) + termcolor.colored("Fine", "green") * (not alert))

    global dataArr, activeFile
    dataArr = array
    activeFile = True

def viewArray():
    print("Name                Catagory            Visits              Days Open           Min Height(m)       Service Status")
    totalVisits = 0
    for i in range(len(dataArr)):
        out = ""
        totalVisits += dataArr[i][2]
        for j in range(len(dataArr[i])):
           out += str(dataArr[i][j]) + (" " * (15 - len(str(dataArr[i][j]))))
           out += "     "
        print(out)
    print(f"Total visits: {totalVisits}")
    input("Press enter to continue ")

def sortArray():
    methodList = {"n" : 0, "c" : 1, "v" : 2, "d" : 3, "h" : 4, "s" : 5}
    reverseList = {"f" : 0, "b" : 1}
    while True:
        method = str(input("What would you like the list to be sorted by?\nName (N), Catagory (C), Visits (V), Days open(D), Minimum Height(H) or Service Status(S): ")).lower()
        print("\n")
        if method in methodList:
            break
        os.system('cls')
        print("Please enter either N, C, V, D, H or S\n")
    while True:
        reverse = str(input("Would you like the list sort forwards (A-Z, 1-9, False-True) or backwards (Z-A, 9-1, True-False)? F/B: ")).lower()
        print("\n")
        if reverse in reverseList:
            break
        os.system('cls')
        print("Please enter either F or B\n")
    global dataArr
    dataArr = sorted(dataArr, key = lambda x: x[methodList[method]], reverse = reverseList[reverse])
    input("Press enter to continue ")

def closeArray():
    global dataArr, activeFile
    dataArr = None
    activeFile = False

while True:
    try:
        if not activeFile:
            actionList = {"1" : getArray, "2" : quit}
        else:
            actionList = {"1" : getArray, "2" : viewArray, "3" : sortArray, "4" : closeArray, "5" : quit}
            print(f"Currently viewing: {fileName}.txt")
        action = str(input(f"What action would you like to do?\n1: Select a {'new ' * activeFile}file to view{(nL+'2: Quit') * (not activeFile)}{(nL+'2: View the file data'+nL+'3: Choose sorting options'+nL+'4: Close the current file'+nL+'5: Quit') * activeFile}\n"))
        if action in actionList:
            os.system('cls')
            actionList[action]()
            os.system('cls')
        else:
            raise
    except:
        print("\nThat wasn't a valid input, please enter the number corresponding to the action you would like to take\n")