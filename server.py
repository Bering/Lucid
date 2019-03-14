import router
from request import Request
from http.server import BaseHTTPRequestHandler

class LucidServer(BaseHTTPRequestHandler):

	def do_HEAD(self):
		return

	def do_GET(self):
		req = Request(self, "get")
		self.respond(router.get_response(req))

	def do_POST(self):
		req = Request(self, "post")
		self.respond(router.get_response(req))

	def do_DELETE(self):
		req = Request(self, "delete")
		self.respond(router.get_response(req))

	def respond(self, response):
		self.send_response(response.status)
	
		for header, value in response.headers.items():
			self.send_header(header, value)
		self.end_headers()
	
		if response.content:
			self.wfile.write(response.content)
