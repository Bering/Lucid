import os
import config
from email.utils import parsedate_tz, mktime_tz

class Response:
	def __init__(self, status, headers, content):
		self.status = status
		self.headers = headers
		self.content = content

class Response204NoContent(Response):
	def __init__(self):
		super().__init__(
			204,
			{},
			""
		)

class Response301Redirect(Response):
	def __init__(self, location):
		super().__init__(
			301,
			{ "Location" : location },
			""
		)

class Response304NotModified(Response):
	def __init__(self, location):
		super().__init__(
			304,
			{},
			""
		)

class Response400BadRequest(Response):
	def __init__(self):
		super().__init__(
			400,
			{ "Content-type" : "text/plain" },
			bytes("400 Bad Request", "UTF-8")
		)

class Response404NotFound(Response):
	def __init__(self):
		super().__init__(
			404,
			{ "Content-type" : "text/plain" },
			bytes("404 Not Found", "UTF-8")
		)

class ResponseJSON(Response):
	def __init__(self, json):
		super().__init__(
			200,
			{ "Content-type" : "text/json" },
			bytes(json, "UTF-8")
		)

class ResponseFile(Response):
	def __init__(self, request, filepath):

		last_modified = os.path.getmtime(filepath)

		#if "If-Modified-Since" in request.base.headers:
		#	since_when = request.base.headers["If-Modified-Since"]
		#	timestamp = mktime_tz(parsedate_tz(since_when))
		#	if last_modified > timestamp:
		#		super().__init__(
		#			304,
		#			{
		#				"Date" : request.base.date_time_string(),
		#				"Content-Location" : request.path
		#			},
		#			""
		#		)
		#		return
		
		filetypes = {
			"html" : ["text/html", "r"],
			"css" : ["text/css", "r"],
			"js" : ["application/javascript", "r"],
			"png" : ["image/png", "rb"],
			"jpg" : ["image/jpeg", "rb"],
		}

		extension = filepath.lower().rsplit(".", 2)[-1]
		if extension in filetypes:
			content_type = filetypes[extension][0]
			mode = filetypes[extension][1]
		else:
			content_type = "text/plain"
			mode = "r"

		headers = {
			"Content-type" : content_type,
			"Last-Modified" : request.base.date_time_string(last_modified)
		}

		fh = open(filepath, mode)
		file_contents = fh.read()

		if mode == "rb":
			content = file_contents
		else:
			content = bytes(file_contents, "UTF-8")

		super().__init__(200, headers, content)

class ResponseView(Response):
	def __init__(self, viewname, replacements={}):
		try:
			content  = self.load_view("header")
			content += self.load_view(viewname)
			content += self.load_view("footer")
		except FileNotFoundError:
			content = "<h1>View file not found!</h1>" + viewname

		for needle, replacement in replacements.items():
			content = content.replace(needle, replacement)

		headers = { "Content-type" : "text/html" }
		content = bytes(content, "UTF-8")
		super().__init__(200, headers, content)

	def load_view(self, viewname):
		filepath = os.path.join(config.path, "views", viewname + ".html")
		fh = open(filepath, "r")
		return fh.read()
