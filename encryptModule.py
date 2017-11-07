import wave, multiprocessing
from constant import *

########################################################################################################################

def eccEncryption():
    os.chdir(JAVA_SOURCE_DIRECTORY)
    os.system("java -cp \"%s*:./\" %s %s %s %s" % (JAR_DIRECTORY, JAVA_ENCRYPTION_CLASS, PUBLIC_KEY_UPLOADED, INFORMATION_IMAGE_UPLOADED, ENCRYPTED_IMAGE_TXT))
    os.chdir(PROJECT_DIRECTORY)

########################################################################################################################
queue = multiprocessing.Queue()

def parallel(n, frames, byteArray):
    tempFrames = ""
    for eachByte in byteArray:
        eightFrames, frames = frames[0:8], frames[8:]
        for i in range(8):
            if eachByte[i] == 0:
                tempFrames = tempFrames + eightFrames[i]
            else:
                asci = ord(eightFrames[i])
                if asci >= 128:
                    tempFrames = tempFrames + chr(asci - 1)
                else:
                    tempFrames = tempFrames + chr(asci + 1)
    queue.put((n, tempFrames ))


def audioStegnography(inputFile, baseWave, outputWave):
    byteArray = []
    with open(inputFile, "rb") as myFile:
        ext = os.path.splitext(inputFile)[1]
        ext = ext + ' ' * (8 - len(ext))
        text = ext + myFile.read()
    for eachCharacter in text:
        byteArray.append(BINARY[ord(eachCharacter)])
    byteArray = byteArray + EOF
    size = len(byteArray)
    audioInput = wave.open(baseWave, "r")
    props = audioInput.getparams()
    capacity = props[3]/4
    logging.warning( "FILE SIZE : %d bytes | File : %s"% (size, inputFile))
    logging.warning( "WAVE CAPACITY : %d bytes | File : %s"%(capacity, baseWave))
    if size > capacity:
        raise Exception("BASE NOT LONG ENOUGH ERROR")
    oldFrames = audioInput.readframes(props[3])
    audioInput.close()

    procs = []

    indicer = len(byteArray) / N_PROC

    requiredFrames = oldFrames[0:len(byteArray) * 8]

    for i in range(N_PROC):
        start, stop = (indicer * i), (indicer * (i + 1))
        if i == N_PROC - 1:
            stop = len(byteArray)
        frame = requiredFrames[start * 8: stop * 8]
        byte = byteArray[start : stop]
        p = multiprocessing.Process(target=parallel, args=(i, frame, byte,))
        procs.append(p)
        p.start()

    result, newFrames = [queue.get() for p in procs], oldFrames
    finalResult = {}
    for tempResult in result:
        finalResult[tempResult[0]] = tempResult[1]

    for i in range(N_PROC):
        newFrames = newFrames + finalResult[i]
    newFrames = newFrames + oldFrames[len(byteArray) * 8:]

    audioOutput = wave.open(outputWave, "w")
    audioOutput.setparams(props)
    audioOutput.setnframes(2 * props[3])
    audioOutput.writeframes(newFrames)
    audioOutput.close()

########################################################################################################################

def generateWave():
    logging.warning( str(datetime.now())+ " CALLING ENCRYPTION")
    eccEncryption()
    logging.warning( str(datetime.now())+ " encryption finished | CALLING STEGANOGRAPHY")
    os.chdir(INPUT_AUDIO_DIRECTORY)
    files = os.listdir('.')
    for file in files:
        try:
            audioStegnography(ENCRYPTED_IMAGE_TXT, file, AUDIO_FILE)
            break
        except Exception, e:
            if str(e) != "BASE NOT LONG ENOUGH ERROR":
                raise Exception(str(e) + " : ", file)

    logging.warning( str(datetime.now())+ " steganography finished")