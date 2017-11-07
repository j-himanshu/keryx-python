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
    logging.warning( str(datetime.now())+" PUBLIC KEY UPLOAD")
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
    logging.warning( str(datetime.now())+" INFORMATION UPLOAD")
    try:
        upload = request.files.get('file')
        name, ext = os.path.splitext(upload.filename)
        if ext != '.png':
            return "File extension not allowed - USE .png"
        upload.save(INFORMATION_IMAGE_UPLOADED)
        return "Your Information Image has been uploaded and is being processed."
    except Exception, e:
        return str(e)

@route('/keryx/uploadPrivateKey', method='POST')
def uploadPrivateKey():
    logging.warning( str(datetime.now())+" PRIVATE KEY UPLOAD")
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
    logging.warning(str(datetime.now())+" AUDIO UPLOAD")
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
        logging.warning( str(datetime.now())+ " KEY DOWNLOAD SERVICE")
        keyGenerateService()
        return static_file("key.zip", PROJECT_DIRECTORY + "generated/key/")
    except Exception, e:
        return str(e)

@route('/keryx/generateAudio')
def audioGenerate():
    try:
        logging.warning( str(datetime.now())+" WAVE GENERATE SERVICE")
        audioGenerateService()
        return static_file("audio.html", root=PROJECT_DIRECTORY)
    except Exception, e:
        return str(e)

@route('/keryx/downloadAudio')
def audioDownload():
    try:
        logging.warning( str(datetime.now())+" WAVE DOWNLOAD SERVICE")
        return static_file("audio.wav", PROJECT_DIRECTORY + "generated/wav/")
    except Exception, e:
        return str(e)

@route('/keryx/generateImage')
def audioGenerate():
    try:
        logging.warning( str(datetime.now())+" IMAGE GENERATE SERVICE")
        imageGenerateService()
        return static_file("image.html", root=PROJECT_DIRECTORY)
    except Exception, e:
        return str(e)

@route('/keryx/downloadImage')
def imageDownload():
    try:
        logging.warning( str(datetime.now())+ " IMAGE DOWNLOAD SERVICE")
        return static_file("image.png", PROJECT_DIRECTORY + "generated/image/")
    except Exception, e:
        return str(e)

########################################################################################################################

@get('/keryx/cleanup')
def cleanup():
    logging.warning(str(datetime.now())+" System Cleanup")
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

@get('/keryx/viewLogs')
def log():
    logging.warning( str(datetime.now())+" Log files requested")
    os.chdir(HOME_DIRECTORY)
    with open("nohup.out", "r") as logger:
        logs = logger.read()
    os.chdir(PROJECT_DIRECTORY)
    with open("log.html", "w") as log:
        log.write("<head><title>KERYX MESSAGING SYSTEM</title></head><body><h1>LOG FILES TILL %s</h1><br/><hr/><br/>" % (str(datetime.now())))
        allLogs = logs.split('\n')
        for eachLog in allLogs:
            log.write(eachLog + "<br/>")
        log.write("</body>")
    return static_file("log.html", root=PROJECT_DIRECTORY)

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

@route('/keryx/viewLogs', method=['OPTIONS'])
def handleOption():
    if request.method == 'OPTIONS':
        return {}

########################################################################################################################
def main():
    run(host = HOST, port = PORT)

if __name__ == "__main__":
    main()