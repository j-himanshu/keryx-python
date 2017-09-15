import os

from keryxRest import main

os.system("sudo iptables -A PREROUTING -t nat -p tcp --dport 80 -j REDIRECT --to-port 5000")
a = os.fork()
if a == 0:
	os.chdir("/home/ubuntu/keryx-react")
	while True:
		if "node /usr/local/bin/serve -s build" not in os.popen("ps -aux | grep node").read():
			os.system("serve -s build &")
else:
	main()