import wave
from constant import *

########################################################################################################################

def eccEncryption():
    os.chdir(JAVA_SOURCE_DIRECTORY)
    os.system("java -cp \"%s*:./\" %s %s %s %s" % (JAR_DIRECTORY, JAVA_ENCRYPTION_CLASS, PUBLIC_KEY_UPLOADED, INFORMATION_IMAGE_UPLOADED, ENCRYPTED_IMAGE_TXT))
    os.chdir(PROJECT_DIRECTORY)

########################################################################################################################

def getBytes(file):
    byte = []
    with open(file, "r") as myFile:
        text = myFile.read()
        print datetime.now(), "ENCRYPT TXT FILE SIZE: ", len(text)
    for eachCharacter in text:
        byte.append(BINARY[ord(eachCharacter)])
    byte = byte + EOF
    return byte

def audioStegnography():
    print datetime.now(), "AUDIO STEGANOGRAPHY STARTED"
    byteArray = getBytes(ENCRYPTED_IMAGE_TXT)
    noOfBits = len(byteArray) * 8
    print datetime.now(), "NUMBER OF BITS: ", noOfBits
    while True:
        audioInputFile = getRandomFile(INPUT_AUDIO_DIRECTORY)
        audioInput= wave.open(audioInputFile, "r")
        props = audioInput.getparams()
        print datetime.now(), "random : ", audioInputFile, " | capacity : ", props[3]
        if noOfBits < props[3]:
            print datetime.now(), "Audio base selected:", audioInputFile
            break
        audioInput.close()
    audioOutput = wave.open(AUDIO_FILE, "w")
    audioOutput.setparams(props)
    audioOutput.setnframes(2 * props[3])
    oldFrames = audioInput.readframes(props[3])
    audioInput.rewind()
    newFrames = oldFrames
    tempFrames = ""
    for eachByte in byteArray:
        eightFrames, newFrames = newFrames[0:8], newFrames[8:]
        for i in range(8):
            if eachByte[i] == 0:
                tempFrames = tempFrames + eightFrames[i]
            else:
                asci = ord(eightFrames[i])
                if asci >= 128:
                    tempFrames = tempFrames + chr(asci - 1)
                else:
                    tempFrames = tempFrames + chr(asci + 1)

    newFrames = oldFrames + tempFrames + newFrames

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