import os

os.system("sudo iptables -A PREROUTING -t nat -p tcp --dport 80 -j REDIRECT --to-port 5000")
a = os.fork()
if a == 0:
    os.chdir("/home/ubuntu/keryx-react")
    os.system("git pull origin master")
    os.system("sudo npm install axios")
    os.system("sudo npm install")
    os.system("sudo npm run build")
    while True:
        if "node /usr/local/bin/serve -s build" not in os.popen("ps -aux | grep node").read():
            os.system("serve -s build &")
else:
    os.chdir("/home/ubuntu/keryx-python")
    os.system("git pull origin master")
    os.system("python keryxRest.py &")
