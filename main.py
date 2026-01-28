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
    ran = random.randint(0, 3)
    if ran > 2:
        return str(random.randint(topOfRange, bottomOfRange)) #range of numbers
    else:
        return getRandomWord()
    


def createRandomLine():
    randomStr = ""
    for i in range(10):
        randomStr += getRandom() + " "  
    return randomStr + "\n" 



def main():
    RandomFileName = "RandomFile"
    
    for i in range(5): #this just adds a string of random numbers at the end to prevent conflicts
        fileNumber = random.randint(0, 9)
        RandomFileName += str(fileNumber)  
    
    RandomFileName += ".txt" #add file type
    
    fileLength = random.randint(1, 1000) #sets length of file (anywhere between 1 and 1000 lines)
    
    try:
        with open(RandomFileName, "w") as file:
            for i in range(fileLength):
                file.write(createRandomLine())
        print(f"File '{RandomFileName}' created successfully with {fileLength} lines!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
