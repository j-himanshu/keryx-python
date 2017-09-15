from decryptModule import decryptMessage
from encryptModule import sendMessage
from getKeyModule import getKey


def keyGenerateService(data):
    return getKey(data)

def messageService(data):
    return sendMessage(data)

def decryptMessageService(data):
    return decryptMessage(data)