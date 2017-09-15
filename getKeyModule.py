import os

from constant import PROJECT_DIRECTORY
from emailModule import sendMail

KEY_FILE_IMAGE = PROJECT_DIRECTORY + "generated/image/key.jpg"
KEY_IMAGE_WAREHOUSE = PROJECT_DIRECTORY + "warehouse/image/"

def keygen():
    #generates publickey, privatekey for ECC
    return (12345678, 87654321)

def embedImage(publicKey):
    #embed publicKey in image - image stegnography
    #INPUT IMAGE : RANDOM FROM : warehouse/image
    #OUTPUT IMAGE : "KEY_FILE_IMAGE"
    pass

def getKey(data):
    publicKey, privateKey = keygen()
    embedImage(publicKey)
    sendMail(
        data['plainText'],
        data['senderEmail'],
        data['receiverEmail'],
        data['senderPassword'],
        KEY_FILE_IMAGE, 'jpg')
    os.remove(KEY_FILE_IMAGE)
    return privateKey