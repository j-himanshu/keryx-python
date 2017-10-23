import wave
from constant import *

########################################################################################################################

def eccEncryption():
    os.chdir(JAVA_SOURCE_DIRECTORY)
    os.system("java -cp \"%s*:./\" %s %s %s %s" % (JAR_DIRECTORY, JAVA_ENCRYPTION_CLASS, PUBLIC_KEY_UPLOADED, INFORMATION_IMAGE_UPLOADED, ENCRYPTED_IMAGE_TXT))
    os.chdir(PROJECT_DIRECTORY)

########################################################################################################################

def getBlockBits(asci):
    num, block = ord(asci), []
    for i in range(7, -1, -1):
        block.append(str(int(num/ 2**i)))
        num = num % 2**i
    return block

def getBit(file):
    bits = []
    with open(file, "r") as myFile:
        text = myFile.read()
    for eachCharacter in text:
        bitBlock = getBlockBits(eachCharacter)
        bits = bits + bitBlock
    return bits + EOF

def audioStegnography():
    inputBitmap = getBit(ENCRYPTED_IMAGE_TXT)
    minSizeRequired = len(inputBitmap)
    while True:
        audioInputFile = getRandomFile(INPUT_AUDIO_DIRECTORY)
        audioInput= wave.open(audioInputFile, "r")
        audioOutput = wave.open(AUDIO_FILE, "w")
        props = audioInput.getparams()
        if minSizeRequired < props[3]:
            break
    audioOutput.setparams(props)
    audioOutput.setnframes(2 * props[3])
    oldFrames = audioInput.readframes(props[3])
    audioInput.rewind()
    newFrames = oldFrames
    i, length = 0, len(inputBitmap)
    for frame in oldFrames:
        if i >= len(inputBitmap) or inputBitmap[i] == '0':
            newFrames = newFrames + frame[0]
            #i >= len(inputBitmap) : when the input is completely embedded, append the rest of audio bits
            #without any modification
            #if the data bit to be embedded is 0, apped frame as it is without any modification
        else:
            #if the data bit to be embedded is 1, either increase or decrease the slope of frame by 1
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

########################################################################################################################

def generateWave():
    print datetime.now(), "CALLING ENCRYPTION"
    eccEncryption()
    print datetime.now(), "encryption finished | CALLING STEGANOGRAPHY"
    audioStegnography()
    print datetime.now(), "steganography finished"