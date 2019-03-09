import time
import config
from http.server import HTTPServer
from server import LucidServer

httpd = HTTPServer((config.hostname, config.port), LucidServer)
print(time.asctime(), ": LUCID server started on", config.hostname + ":" + str(config.port))

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass

print(time.asctime(), ": LUCID server shutting down")
httpd.server_close()
