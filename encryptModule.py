def getKey(data):
    # check for uploaded image file
    # do image steganalysis and get public key
    return 12345678


def eccEncryption(data, key):
    # from data, get secret message
    # apply ECC algorithm, and message encrypt using key
    # store the resultant encrypted file, in -"somefile.txt"
    pass


def audioStegnography():
    # read data from "somefile.txt"
    # embed the data in audio file - "somefile.wav"
    pass


def sendMessage(data):
    publicKey = getKey(data)
    eccEncryption(data, publicKey)
    audioStegnography()
    # send email - with attachment "somefile.wav"
