import os
import random

PROJECT_DIRECTORY = "/home/hs/PycharmProjects/keryx-python/"
HOST = "localhost"
PORT = "5001"

def getRandomFile(path):
    files = os.listdir(path)
    return path + files[int(random.random()*10**10) % len(files)]