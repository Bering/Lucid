import router
from http.server import BaseHTTPRequestHandler

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
	
		for header, value in response.headers.items():
			self.send_header(header, value)
		self.end_headers()
	
		if response.content:
			self.wfile.write(response.content)
