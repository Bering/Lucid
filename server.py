import os
from http.server import BaseHTTPRequestHandler
from response import Response
from response_404 import Response404NotFound
from response_file import ResponseFile

class LucidServer(BaseHTTPRequestHandler):

	def do_HEAD(self):
		return

	def do_GET(self):
		filepath = "public" + self.path
		if not os.path.isfile(filepath):
			response = Response404NotFound()
		else:
			response = ResponseFile(filepath)
		self.respond(response)
	
	def do_POST(self):
		return

	def respond(self, response):
		self.send_response(response.status)
		self.send_header("Content-type", response.content_type)
		self.end_headers()
		self.wfile.write(bytes(response.content, "UTF-8"))
