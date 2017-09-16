import os
import random

PROJECT_DIRECTORY = "/home/ubuntu/keryx-python/"
HOST = ""
PORT = "5001"

def getRandomFile(path):
    files = os.listdir(path)
    return path + files[int(random.random()*10**10) % len(files)]