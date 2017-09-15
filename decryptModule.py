import os
import wave

from constant import PROJECT_DIRECTORY

ENCRYPTED_FILE = PROJECT_DIRECTORY + "generated/file/encrypted.txt"
UPLOADED_WAV_AUDIO = PROJECT_DIRECTORY + "upload/wav/audio.wav"

########################################################################################################################

def eccDecryption(privateKey):
    #read "ENCRYPTED_FILE"
    #decrypt the content using the private key
    #read the secret message
    return "secret message"

########################################################################################################################

def getAsciText(bitArray):
    text = ""
    while True:
        byte = bitArray[0:8]
        asci = int(str(byte).replace("[", "").replace("]", "").replace(",", "").replace(" ", ""), 2)
        if asci == 255:
            break
        text = text + chr(asci)
        bitArray = bitArray[8:]
    return text

def stegAnalysis():
    audio = wave.open(UPLOADED_WAV_AUDIO, "r")
    props = audio.getparams()
    originalFrames = audio.readframes(props[3]/2)
    modifiedFrames = audio.readframes(props[3]/2)
    audio.close()
    bitArray = []
    for i in range(len(originalFrames)):
        if originalFrames[i] != modifiedFrames[i]:
            bitArray.append(1)
        else:
            bitArray.append(0)
    information = getAsciText(bitArray)
    with open(ENCRYPTED_FILE, "w") as output:
        output.write(information)

########################################################################################################################

def decryptMessage(data):
    stegAnalysis()
    secret = eccDecryption(data['passkey'])
    os.remove(UPLOADED_WAV_AUDIO)
    os.remove(ENCRYPTED_FILE)
    return secret