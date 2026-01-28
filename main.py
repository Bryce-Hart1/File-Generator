import random
import os

def getRandomWord():
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    words_file = os.path.join(scriptDirectory, "randomWords.txt")
    
    with open(words_file, 'r') as file:
        w = [w.strip() for word in file.readlines()]
        return w




def getRandom():
    ran = random.randint(0,3)
    if ran > 2:
        return random.randint(-9,999,999, 999,999,999) #for now between this range
    else:
        return getRandomWord

def createRandomLine():
    randomStr = ""
    for i in range(10):
        randomStr += getRandom
        return getRandom




def main():
    RandomFileName = "RandomFile"

    for i in range(5):
        fileNumber = random.randint(0, 9)
        RandomFileName + fileNumber

    fileLength = random.randomint(1, 1000)
    try:
        with open(RandomFileName, "w") as file:
            for i in range(fileLength):
                file.writelines(createRandomLine)
    except FileExistsError:
        print("FileExistsError")
