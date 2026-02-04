import random
import os

def getRandomWord():
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    words_file = os.path.join(scriptDirectory, "randomWords.txt")
    
    with open(words_file, 'r') as file:
        words = [word.strip() for word in file.readlines()]
        return random.choice(words)
    


def getRandom():
    topOfRange = 9200000000000000000 #close to 64 bit maximum
    bottomOfRange = -9200000000000000000 #close to 64 bit min
    ran = random.randint(0, 4)
    if ran > 3:
        return str(random.randint(bottomOfRange, topOfRange)) #range of numbers
    else:
        return getRandomWord()
    


def createRandomLine():
    randomStr = ""
    for i in range(10):
        randomStr += getRandom() + " "  
    return randomStr + "\n" 



def main():
    filesToMake = int(input("Enter Number of files to Generate-"))
    for fc in range(filesToMake):
        RandomFileName = "RandomFile"
        for i in range(5): #this just adds a string of random numbers at the end to prevent conflicts
            fileNumber = random.randint(0, 9)
            RandomFileName += str(fileNumber)
        RandomFileName += ".txt" #might add multiple files types later  
    
    
        maxFileLength = random.randint(300, 10000) #sets length of file (anywhere between 1 and 1000 lines)
    
        try:
            with open(RandomFileName, "w") as file:
                for i in range(maxFileLength):
                    file.write(createRandomLine())
            print(f"File '{RandomFileName}' created successfully with {maxFileLength} lines!")
        except Exception as e:
            print(f"Error: {e}")
            filesToMake -1
if __name__ == "__main__":
    main()
