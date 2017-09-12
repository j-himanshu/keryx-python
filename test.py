import wave

projectDirectory = "/home/hs/PycharmProjects/keryx-python/"
secretFile = projectDirectory + "secret.txt"
audioInputFile = projectDirectory + "audioInput.wav"
audioOutputFile = projectDirectory + "audioOutput.wav"

def magic(secret, audioFileName):
    audioFile = wave.open(audioFileName, "r")
    props = audioFile.getparams()
    oldFrames = audioFile.readframes(props[3])
    newFrames = []
    for frame in oldFrames:
        byte = frame[0]
        asci = ord(byte)
        newFrames.append(asci)

def getBlockBits(asci):
    asciVal = ord(asci)
    binary = bin(asciVal)[2:]
    block = [0]*(8-len(binary)) + list(binary)
    return block

def getBit(file):
    bits = []
    with open(file, "r") as myFile:
        text = myFile.read()
    for eachCharacter in text:
        bitBlock = getBlockBits(eachCharacter)
        bits = bits + bitBlock
    return len(bits)

if __name__ == "__main__":
    bitArray = getBit(secretFile)
    magic(bitArray, audioInputFile)