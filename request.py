import cgi

class Request:
	def __init__(self, base_http_request, method):
		self.base = base_http_request
		self.method = method
		self.path = self.base.path
		self.path_parts = self.path[1:].split("/")
		self.form_fields = {}

		if self.method == "post":
			self.form_fields = self.get_form_fields()

	# from https://stackoverflow.com/questions/4233218/python-how-do-i-get-key-value-pairs-from-the-basehttprequesthandler-http-post-h
	def get_form_fields(self):
		ctype, pdict = cgi.parse_header(self.base.headers["content-type"])
		if ctype == "multipart/form-data":
			postvars = cgi.parse_multipart(self.base.rfile, pdict)
		elif ctype == "application/x-www-form-urlencoded":
			length = int(self.base.headers["content-length"])
			postvars = cgi.parse_qs(self.base.rfile.read(length))
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

