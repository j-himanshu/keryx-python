import wave
from constant import *

########################################################################################################################

def eccDecryption():
    os.chdir(JAVA_SOURCE_DIRECTORY)
    os.system("java -cp \"%s*:./\" %s %s %s %s" %
              (JAR_DIRECTORY, JAVA_DECRYPTION_CLASS, PRIVATE_KEY_UPLOADED, ENCRYPTED_IMAGE_TXT, INFORMATION_IMAGE))
    os.chdir(PROJECT_DIRECTORY)

########################################################################################################################

def stegAnalysis():
    audio = wave.open(AUDIO_FILE_UPLOADED, "r")
    props = audio.getparams()
    originalFrames = audio.readframes(props[3]/2)
    modifiedFrames = audio.readframes(props[3]/2)
    audio.close()
    text, previous, byte = "", 0, 0
    for i in range(len(originalFrames) / 8):
        prior = previous
        previous = byte
        byte = 0
        for j in range (8):
            index = 8 * i + j
            byte = byte * 2
            if originalFrames[index] != modifiedFrames[index]:
                byte = byte + 1
        if prior == 204 and previous == 51 and byte == 240:
            break
        text = text + chr(byte)
    text = text[0:-2]
    with open(ENCRYPTED_IMAGE_TXT, "w") as output:
        output.write(text)

########################################################################################################################

def decryptMessage():
    print datetime.now(), "CALLING STEGANALYSIS"
    stegAnalysis()
    print datetime.now(), "steganalysis finished | CALLING ECC DECRYPTION"
    eccDecryption()
    print datetime.now(), "decryption finished"