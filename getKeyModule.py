import os

from steganography.steganography import Steganography

from constant import PROJECT_DIRECTORY, getRandomFile
from emailModule import sendMail

KEY_FILE_IMAGE = PROJECT_DIRECTORY + "generated/image/key.jpg"
KEY_IMAGE_WAREHOUSE = PROJECT_DIRECTORY + "warehouse/image/"

def keygen():
    #generates publickey, privatekey for ECC
    return (12345678, 87654321)

def embedImage(publicKey):
    baseImageFile = getRandomFile(KEY_IMAGE_WAREHOUSE)
    Steganography.encode(baseImageFile, KEY_FILE_IMAGE, publicKey)

def getKey(data):
    publicKey, privateKey = keygen()
    embedImage(publicKey)
    sendMail(
        data['plainMessage'],
        data['senderEmail'],
        data['receiverEmail'],
        data['passkey'],
        KEY_FILE_IMAGE, 'jpg')
    os.remove(KEY_FILE_IMAGE)
    return privateKey