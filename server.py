import cgi
import router
from http.server import BaseHTTPRequestHandler

class LucidServer(BaseHTTPRequestHandler):

	def do_HEAD(self):
		return

	def do_GET(self):
		self.respond(
			router.get_response(
				"get",
				self.path,
				{} # no form_fields for GET requests. I wasted enough time with this shit.. I miss PHP's $_GET and $_POST. I'll only do POST requests for this project and next time I will use a framework anyway...
			)
		)

	def do_POST(self):
		self.respond(
			router.get_response(
				"post",
				self.path,
				self.get_form_fields()
			)
		)

	# from https://stackoverflow.com/questions/4233218/python-how-do-i-get-key-value-pairs-from-the-basehttprequesthandler-http-post-h
	def get_form_fields(self):
		ctype, pdict = cgi.parse_header(self.headers["content-type"])
		if ctype == "multipart/form-data":
			postvars = cgi.parse_multipart(self.rfile, pdict)
		elif ctype == "application/x-www-form-urlencoded":
			length = int(self.headers["content-length"])
			postvars = cgi.parse_qs(self.rfile.read(length))
		else:
			return {}

		form_fields = {}
		for key, value in postvars.items():
			if isinstance(value, list):
				# TODO: Support lists maybe but for now screw them I don't need them
				form_fields[key.decode('UTF-8')] = value[0].decode('UTF-8')
			else:
				form_fields[key.decode('UTF-8')] = value.decode('UTF-8')

		return form_fields

	def respond(self, response):
		self.send_response(response.status)
	
		for header, value in response.headers.items():
			self.send_header(header, value)
		self.end_headers()
	
		if response.content:
			self.wfile.write(response.content)
