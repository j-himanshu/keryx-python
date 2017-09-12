import wave

projectDirectory = "/home/hs/PycharmProjects/keryx-python/"
secretFile = projectDirectory + "secret.txt"
audioInputFile = projectDirectory + "audioInput.wav"
audioOutputFile = projectDirectory + "audioOutput.wav"
EOF = [1, 1, 1, 1, 1, 1, 1, 1]

def magic(secret, audioFileName):
    #open input file - read mode
    audioInput= wave.open(audioFileName, "r")
    #open output file - write mode
    audioOutput = wave.open(audioOutputFile, "w")
    #read input wave properties
    props = audioInput.getparams()
    #set output wave properties
    audioOutput.setparams(props)
    #double the number of output frames
    audioOutput.setnframes(2 * props[3])
    #read all the frames of input wave
    oldFrames = audioInput.readframes(props[3])
    #rewind the wave pointer to the beginning of wave
    audioInput.rewind()
    #replicate original frames to newFrame buffer
    newFrames = oldFrames
    #initialise iterator for data bits
    i, length = 0, len(secret)
    for frame in oldFrames:
        if i >= len(secret) or secret[i] == 0:
            newFrames = newFrames + frame[0]
        else:
            byte = frame[0]
            asci = ord(byte)
            if asci >= 128:
                newFrames = newFrames + (chr(asci - 1))
            else:
                newFrames = newFrames + (chr(asci + 1))
        i = i + 1
    audioOutput.writeframes(newFrames)
    audioOutput.close()
    audioInput.close()

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
    return bits + EOF

if __name__ == "__main__":
    bitArray = getBit(secretFile)
    magic(bitArray, audioInputFile)