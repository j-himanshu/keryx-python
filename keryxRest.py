from bottle import *
from constant import *
from keryxService import *


########################################################################################################################

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

########################################################################################################################

@route('/keryx/uploadPublicKey', method='POST')
def uploadPublicKey():
    print datetime.now(), "PUBLIC KEY UPLOAD"
    try:
        upload = request.files.get('file')
        name, ext = os.path.splitext(upload.filename)
        if ext != '':
            return "Invalid File Extension for key"
        upload.save(PUBLIC_KEY_UPLOADED)
        return "Key Uploaded, we'll encrypt your Information Image shortly"
    except Exception, e:
        return str(e)

@route('/keryx/uploadInformation', method='POST')
def uploadInformation():
    print datetime.now(), "INFORMATION UPLOAD"
    try:
        upload = request.files.get('file')
        name, ext = os.path.splitext(upload.filename)
        if ext not in ['.jpg', '.jpeg']:
            return "File extension not allowed - USE .jpg, .jpeg"
        upload.save(INFORMATION_IMAGE_UPLOADED)
        return "Your Information Image has been uploaded and is being processed."
    except Exception, e:
        return str(e)

@route('/keryx/uploadPrivateKey', method='POST')
def uploadPrivateKey():
    print datetime.now(), "PRIVATE KEY UPLOAD"
    try:
        upload = request.files.get('file')
        name, ext = os.path.splitext(upload.filename)
        if ext != '':
            return "Invalid File Extension for key"
        upload.save(PRIVATE_KEY_UPLOADED)
        return "Key Uploaded, we'll decrypt your Information Image shortly"
    except Exception, e:
        return str(e)

@route('/keryx/uploadAudioFile', method='POST')
def uploadWav():
    print datetime.now(), "AUDIO UPLOAD"
    try:
        upload = request.files.get('file')
        name, ext = os.path.splitext(upload.filename)
        if ext != '.wav':
            return "File extension not allowed - USE .wav"
        upload.save(AUDIO_FILE_UPLOADED)
        return "Audio Uploaded, sit back and relax while we process your audio."
    except Exception, e:
        return str(e)

########################################################################################################################

@route('/keryx/downloadKey')
def keyDownload():
    try:
        print datetime.now(), "KEY DOWNLOAD SERVICE"
        keyGenerateService()
        return static_file("key.zip", PROJECT_DIRECTORY + "generated/key/")
    except Exception, e:
        return str(e)

@route('/keryx/downloadAudio')
def audioDownload():
    try:
        print datetime.now(), "WAVE DOWNLOAD SERVICE"
        audioGenerateService()
        return static_file("audio.wav", PROJECT_DIRECTORY + "generated/wav/")
    except Exception, e:
        return str(e)

@route('/keryx/downloadImage')
def imageDownload():
    try:
        print datetime.now(), "IMAGE DOWNLOAD SERVICE"
        imageGenerateService()
        return static_file("image.jpg", PROJECT_DIRECTORY + "generated/image/")
    except Exception, e:
        return str(e)

########################################################################################################################

@get('/keryx/cleanup')
def cleanup():
    directories = [PROJECT_DIRECTORY + "generated/key/",
               PROJECT_DIRECTORY + "generated/image/",
               PROJECT_DIRECTORY + "generated/wav/",
               PROJECT_DIRECTORY + "generated/txt/",
               PROJECT_DIRECTORY + "upload/key/",
               PROJECT_DIRECTORY + "upload/image/",
               PROJECT_DIRECTORY + "upload/wav/"]
    for eachDirectory in directories:
        os.chdir(eachDirectory)
        os.system("rm *")

    return "SUCCESSFUL ROUTINE CLEANUP"

########################################################################################################################

@route('/keryx/uploadPublicKey', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

@route('/keryx/uploadAudioFile', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

@route('/keryx/uploadInformation', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

@route('/keryx/uploadPrivateKey', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

@route('/keryx/cleanup', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

########################################################################################################################
def main():
    run(host = HOST, port = PORT)

if __name__ == "__main__":
    main()