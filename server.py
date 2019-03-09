import os
import router
from http.server import BaseHTTPRequestHandler
from response import Response

class LucidServer(BaseHTTPRequestHandler):

	def do_HEAD(self):
		return

	def do_GET(self):
		response = router.get_response(self.path)
		self.respond(response)
	
	def do_POST(self):
		return

	def respond(self, response):
		self.send_response(response.status)
		self.send_header("Content-type", response.content_type)
		self.end_headers()
		self.wfile.write(bytes(response.content, "UTF-8"))
