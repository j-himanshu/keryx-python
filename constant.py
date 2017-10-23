import os
import random
from datetime import *

HOME_DIRECTORY = "/Users/hs/"
PROJECT_DIRECTORY = HOME_DIRECTORY + "PycharmProjects/keryx-python/"
JAVA_SOURCE_DIRECTORY = HOME_DIRECTORY + "IdeaProjects/keryx-ecc/src"
JAR_DIRECTORY = HOME_DIRECTORY + "IdeaProjects/commons-io-2.6/"
PROJECT_UPLOAD_DIRECTORY = PROJECT_DIRECTORY + "upload/"
INPUT_AUDIO_DIRECTORY = PROJECT_DIRECTORY + "audioWarehouse/"

JAVA_KEY_GENERATE_CLASS = "com.keryx.ecc.TestECCrypto"
JAVA_ENCRYPTION_CLASS = "com.keryx.ecc.testImageCrypto"
JAVA_DECRYPTION_CLASS = "com.keryx.ecc.testDecryptImage"

PRIVATE_KEY = PROJECT_DIRECTORY + "generated/key/privatekey"
PUBLIC_KEY = PROJECT_DIRECTORY + "generated/key/publickey"
INFORMATION_IMAGE = PROJECT_DIRECTORY + "generated/image/image.jpg"
AUDIO_FILE = PROJECT_DIRECTORY + "generated/wav/audio.wav"

ZIP_FILE = PROJECT_DIRECTORY + "generated/key/key.zip"
ENCRYPTED_IMAGE_TXT = PROJECT_DIRECTORY + "generated/txt/encrypt.txt"

PRIVATE_KEY_UPLOADED = PROJECT_DIRECTORY + "upload/key/privatekey"
PUBLIC_KEY_UPLOADED = PROJECT_DIRECTORY + "upload/key/publickey"
INFORMATION_IMAGE_UPLOADED = PROJECT_DIRECTORY + "upload/image/image.jpg"
AUDIO_FILE_UPLOADED = PROJECT_DIRECTORY + "upload/wav/audio.wav"

EOF = ['1', '1', '0', '0', '1', '1', '0', '0',
       '0', '0', '1', '1', '0', '0', '1', '1',
       '1', '1', '1', '1', '0', '0', '0', '0']
HOST = ""
PORT = "8080"

def getRandomFile(path):
    files = os.listdir(path)
    return path + files[int(random.random()*10**10) % len(files)]