import sys
import hashlib
from pathlib import Path
from datetime import datetime
from os.path import exists


def hash():
    global inputType
    global inputName
    global inputChecksum
    inputType = ""
    inputName = ""
    inputChecksum = ""
    if len(sys.argv) < 2:
        print("Error: require two arguments!")
        x = input("Enter arguments: ").split(" ")
    else:
        if sys.argv[1] in ["-h", "h", "-help", "--h", "--help"]:
            print("============================= \n"
                  "           hash.py            \n"
                  " -f [file]         -t [text]  \n"
                  "============================= \n")
        elif sys.argv[1] in ["-f", "-t"]:
            x = []
            for i in range(1, len(sys.argv)):
                x.append(sys.argv[i])
        else:
            x = input("Enter arguments: ").split(" ")

    if x[0] == "-t":
        for i in range(len(x)):
            if i == 0:
                continue
            if i != (len(x) - 1):
                inputName += x[i] + " "
            else:
                inputName += x[i]
        inputType = "text"
        inputChecksum = hashlib.md5(inputName.encode()).hexdigest()
        print(inputChecksum)
        logPerm()
    elif x[0] == "-f":
        inputType = "file"
        inputName = x[1]
        try:
            if x[2] != None:
                print("Only taking first argument " + str(x[1]) + " for files!")
        except Exception:
            pass
        try:
            inputChecksum = hashlib.md5(open(Path((x[1])), 'rb').read()).hexdigest()
        except Exception:
            print("Error! Please make sure you entered a valid file path.")
            sys.exit()
        print(inputChecksum)
        logPerm()
    else:
        print("============================= \n"
              "           hash.py            \n"
              " -f [file]         -t [text]  \n"
              "============================= \n")


def logPerm():
    global inputType
    global inputName
    global inputChecksum
    if exists("log.txt"):
        with open("log.txt") as f:
            line = f.readline().rstrip()
            if line == "b4a7685b18b84720f09751b97b5f9859":
                logWrite()
                return
            f.close()
        response = input("File 'log.txt' already exists! Are you sure you would like this program to write to it? Y "
                         "or N ")
        if response.lower() == "y":
            print("Permission granted! Overwriting log file...")
            f = open("log.txt", "w")
            f.write("b4a7685b18b84720f09751b97b5f9859\n")
            f.close()
            logWrite()
        else:
            print("No permission given, exiting...")
            sys.exit()


def logWrite():
    global inputType
    global inputName
    global inputChecksum

    f = open("log.txt", "a")
    f.write("Hashed " + inputType + " named \"" + inputName + "\" with checksum " + inputChecksum + " at " + str(
        datetime.utcnow()) + "!\n")
    f.close()


hash()
