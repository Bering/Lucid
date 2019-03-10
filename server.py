import router
from http.server import BaseHTTPRequestHandler

class LucidServer(BaseHTTPRequestHandler):

	def do_HEAD(self):
		return

	def do_GET(self):
		self.respond(router.get_response("get", self.path))

	def do_POST(self):
		self.respond(router.get_response("post", self.path))

	def respond(self, response):
		self.send_response(response.status)
	
		for header, value in response.headers.items():
			self.send_header(header, value)
		self.end_headers()
	
		if response.content:
			self.wfile.write(response.content)
