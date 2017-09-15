from bottle import *

from keryxService import *

IMAGE_PATH = "/home/hs/PycharmProjects/keryx-python/upload/image/"
AUDIO_PATH = "/home/hs/PycharmProjects/keryx-python/upload/wav/"

########################################################################################################################

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

########################################################################################################################

@route('/keryx/uploadKeyImage', method='POST')
def uploadKey():
    try:
        upload = request.files.get('file')
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png', '.jpg', '.jpeg'):
            return "File extension not allowed - USE .png .jpg .jpeg"
        if not os.path.exists(IMAGE_PATH):
            os.makedirs(IMAGE_PATH)
        file_path = "{path}/{file}".format(path=IMAGE_PATH, file=upload.filename)
        upload.save(file_path)
        return "Key Uploaded"
    except Exception, e:
        return str(e)

@route('/keryx/uploadAudioFile', method='POST')
def uploadWav():
    try:
        upload = request.files.get('file')
        name, ext = os.path.splitext(upload.filename)
        if ext != '.wav':
            return "File extension not allowed - USE .wav"
        if not os.path.exists(AUDIO_PATH):
            os.makedirs(AUDIO_PATH)
        file_path = "{path}/{file}".format(path=AUDIO_PATH, file=upload.filename)
        upload.save(file_path)
        return "Key Uploaded"
    except Exception, e:
        return str(e)

########################################################################################################################

@post('/keryx/generateKey')
def generateKeyRest():
    try:
        publicKey = keyGenerateService(request.json)
        return {'status' : True, 'key' : publicKey}
    except Exception, e:
        return {'status': False, 'message': str(e)}

@post('/keryx/sendMessage')
def sendMessageRest():
    try:
        messageService(request.json)
        return {'status': True, 'message': "Message has been sent"}
    except Exception, e:
        return {'status': False, 'message': str(e)}

@post('/keryx/decryptMessage')
def decryptMessageRest():
    try:
        message = decryptMessageService(request.json)
        return {'status': True, 'message': message}
    except Exception, e:
        return {'status': False, 'message': str(e)}

########################################################################################################################

@route('/keryx/uploadKeyImage', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}\

@route('/keryx/uploadAudioFile', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

@route('/keryx/generateKey', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

@route('/keryx/sendMessage', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

@route('/keryx/decryptMessage', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

########################################################################################################################

if __name__ == "__main__":
    run(host='localhost', port=5001)