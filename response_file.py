import os
from response import Response

class ResponseFile(Response):

	def __init__(self, filepath):

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

		f = open(filepath, mode)
		content = f.read()

		if mode == "rb":
			super().__init__(200, content_type, content)
		else:
			super().__init__(200, content_type, bytes(content, "UTF-8"))
