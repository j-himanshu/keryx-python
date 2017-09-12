import wave

def magic(audioFileName):
    audioFile = wave.open(audioFileName, "r")
    props = audioFile.getparams()
    oldFrames = audioFile.readframes(props[3])
    newFrames = []
    for frame in oldFrames:
        byte = frame[0]
        char = chr(byte)
        asci = ord(char)