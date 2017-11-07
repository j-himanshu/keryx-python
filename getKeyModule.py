from constant import *

def getKey():
    # NOTE: FOR FIRST TIME COMPILATION AND CLASS GENERATION USE THE FOLLOWING COMMAND
    os.chdir(JAVA_SOURCE_DIRECTORY)
    os.system("javac com/keryx/ecc/*.java -cp \"%s*:./\"" % (JAR_DIRECTORY))
    os.system("java -cp \"%s*:./\" %s %s %s" % (JAR_DIRECTORY, JAVA_KEY_GENERATE_CLASS, PUBLIC_KEY, PRIVATE_KEY))
    os.system("zip %s %sgenerated/key/*" % (ZIP_FILE, PROJECT_DIRECTORY))
    logging.warning( str(datetime.now())+ " KEYS GENERATED")