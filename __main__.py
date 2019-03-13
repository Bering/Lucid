import sys
import time
import getopt
from config import Config
from http.server import HTTPServer
from server import LucidServer

config = Config()
user_config = config.load()
hostname = user_config["hostname"]
port = user_config["port"]

usage = 'LUCID -p <port> <hostname> or <hostname:port>'
try:
	opts, args = getopt.getopt(sys.argv[1:],"hp:",["port="])
except getopt.GetoptError:
	print (usage)
	sys.exit(2);
for opt, arg in opts:
	if opt == '-h':
		print (usage)
		sys.exit();
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
	print("Config saved: hostname=" + hostname + ", port=" + str(port) + " in file: ", config.config_file)
	port = int(port)
	config.save(hostname, port)

httpd = HTTPServer((hostname, port), LucidServer)
print(time.asctime(), ": LUCID server started on", hostname + ":" + str(port))

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass

print(time.asctime(), ": LUCID server shutting down")
httpd.server_close()
