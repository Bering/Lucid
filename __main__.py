import os
import sys
import time
import getopt
import router
import config
import webbrowser
from bottle import TEMPLATE_PATH, run

cfg = config.Config()
user_config = cfg.load()
hostname = user_config["hostname"]
port = user_config["port"]
debug = False

usage = 'LUCID -d -p <port> <hostname> or <hostname:port>'
try:
	opts, args = getopt.getopt(sys.argv[1:],"hdp:",["port=","debug"])
except getopt.GetoptError:
	print (usage)
	sys.exit(2);
for opt, arg in opts:
	if opt == '-h':
		print (usage)
		sys.exit();
	elif opt in ("-d", "--debug"):
		debug = True
	elif opt in ("-p", "--port"):
		port = arg
if len(args):
	hostname = args[0]

if "-p" not in opts and "--port" not in opts:
	hostname_parts = hostname.split(":")
	if len(hostname_parts) == 2:
		hostname = hostname_parts[0]
		port = hostname_parts[1]

if len(sys.argv) > 1:
	port = int(port)
	cfg.save(hostname, port)

print(time.asctime(), ": LUCID server started on", hostname + ":" + str(port) + " debug:" + str(debug))

TEMPLATE_PATH.insert(0, os.path.join(config.path, "views"))
try:
	webbrowser.open("http://"+hostname+":"+str(port))
	run(host=hostname, port=port, debug=debug)

except KeyboardInterrupt:
	pass

print(time.asctime(), ": LUCID server shutting down")
