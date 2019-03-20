import os
import sys
import time
import getopt
import router
import config
import webbrowser
from bottle import TEMPLATE_PATH, run

def parse_arguments(hostname, port, debug):
	usage = """
	Usage: LUCID [<hostname>] [<hostname:port>]\n\
	             [-p port] [--port port]\n\
	             [-d] [--debug]
	"""

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

	return hostname, port, debug


config_manager = config.ConfigManager()
hostname, port = config_manager.load()
hostname, port, debug = parse_arguments(hostname, port, False)
if len(sys.argv[1:]):
	config_manager.save(hostname, port)

TEMPLATE_PATH.insert(0, os.path.join(config.path, "views"))

print(time.asctime(), ": LUCID server started on", hostname + ":" + str(port) + " debug:" + str(debug))

try:
	webbrowser.open("http://"+hostname+":"+str(port))
	run(host=hostname, port=port, debug=debug)

except KeyboardInterrupt:
	pass

print(time.asctime(), ": LUCID server shutting down")
