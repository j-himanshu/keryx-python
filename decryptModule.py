import wave
from constant import *

########################################################################################################################

def eccDecryption():
    os.chdir(JAVA_SOURCE_DIRECTORY)
    os.system("java -cp \"%s*:./\" %s %s %s %s" %
              (JAR_DIRECTORY, JAVA_DECRYPTION_CLASS, PRIVATE_KEY_UPLOADED, ENCRYPTED_IMAGE_TXT, INFORMATION_IMAGE))
    os.chdir(PROJECT_DIRECTORY)

########################################################################################################################

def stegAnalysis(inputFile):
    audio = wave.open(inputFile, "rb")
    props = audio.getparams()
    originalFrames = audio.readframes(props[3] / 2)
    modifiedFrames = audio.readframes(props[3] / 2)
    audio.close()
    text, previous, byte = "", 0, 0
    for i in range(len(originalFrames) / 8):
        prior = previous
        previous = byte
        byte = 0
        for j in range(8):
            index = 8 * i + j
            byte = byte * 2
            if originalFrames[index] != modifiedFrames[index]:
                byte = byte + 1
        if prior == A and previous == B and byte == C:
            break
        text = text + chr(byte)
    # filename = ("outputFile" + text[0:8]).replace(' ', '')
    text = text[8:-2]
    # with open(filename, "w") as output:
    #     output.write(text)
    with open(ENCRYPTED_IMAGE_TXT, "wb") as output:
        output.write(text)

########################################################################################################################

def decryptMessage():
    logging.warning( str(datetime.now())+" CALLING STEGANALYSIS")
    stegAnalysis(AUDIO_FILE_UPLOADED)
    logging.warning( str(datetime.now())+" steganalysis finished | CALLING ECC DECRYPTION")
    eccDecryption()
    logging.warning( str(datetime.now())+" decryption finished")