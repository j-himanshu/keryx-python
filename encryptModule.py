import os
import wave

from constant import PROJECT_DIRECTORY, getRandomFile
from emailModule import sendMail

INPUT_AUDIO_DIRECTORY = PROJECT_DIRECTORY + "warehouse/wav/"
ENCRYPTED_FILE = PROJECT_DIRECTORY + "generated/file/encrypted.txt"
AUDIO_OUTPUT_FILE = PROJECT_DIRECTORY + "generated/wav/audio.wav"
UPLOADED_KEY_IMAGE_FILE = PROJECT_DIRECTORY + "upload/image/key.jpg"
EOF = ['1', '1', '1', '1', '1', '1', '1', '1']

########################################################################################################################

def getKey():
    # check for uploaded image file : "UPLOADED_KEY_IMAGE_FILE"
    # do image steganalysis and get public key
    return 12345678


def eccEncryption(secretData, key):
    # from data, get secret message
    # apply ECC algorithm, and message encrypt using key
    # store the resultant encrypted file, in : "ENCRYPTED_FILE"
    with open(ENCRYPTED_FILE, "w") as encryptedFile:
        encryptedFile.write(secretData)

########################################################################################################################

def getBlockBits(asci):
    asciVal = ord(asci)
    binary = bin(asciVal)[2:]
    block = ['0']*(8-len(binary)) + list(binary)
    return block

def getBit(file):
    bits = []
    with open(file, "r") as myFile:
        text = myFile.read()
    for eachCharacter in text:
        bitBlock = getBlockBits(eachCharacter)
        bits = bits + bitBlock
    return bits + EOF

def audioStegnography(inputFile):
    inputBitmap = getBit(inputFile)
    audioInputFile = getRandomFile(INPUT_AUDIO_DIRECTORY)
    audioInput= wave.open(audioInputFile, "r")
    audioOutput = wave.open(AUDIO_OUTPUT_FILE, "w")
    props = audioInput.getparams()
    audioOutput.setparams(props)
    audioOutput.setnframes(2 * props[3])
    oldFrames = audioInput.readframes(props[3])
    audioInput.rewind()
    newFrames = oldFrames
    i, length = 0, len(inputBitmap)
    for frame in oldFrames:
        if i >= len(inputBitmap) or inputBitmap[i] == '0':
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

########################################################################################################################

def sendMessage(data):
    publicKey = getKey()
    eccEncryption(str(data['secretMessage']), publicKey)
    audioStegnography(ENCRYPTED_FILE)
    sendMail(
        data['plainMessage'],
        data['senderEmail'],
        data['receiverEmail'],
        data['passkey'],
        AUDIO_OUTPUT_FILE, 'wav')
    os.remove(UPLOADED_KEY_IMAGE_FILE)
    os.remove(ENCRYPTED_FILE)
    os.remove(AUDIO_OUTPUT_FILE)
