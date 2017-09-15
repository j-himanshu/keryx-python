def keygen():
    #generates publickey, privatekey for ECC
    return (12345678, 87654321)

def embedImageAndEmail(publicKey, data):
    #read data, fetch sender email id-password,
    #fetch receiver email id, message body
    #embed publicKey in image
    #attach image to email and send email
    pass

def getKey(data):
    publicKey, privateKey = keygen()
    embedImageAndEmail(publicKey, data)
    return privateKey