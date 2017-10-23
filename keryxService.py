from decryptModule import decryptMessage
from encryptModule import generateWave
from getKeyModule import getKey


def keyGenerateService():
    getKey()

def audioGenerateService():
    generateWave()

def imageGenerateService():
    decryptMessage()