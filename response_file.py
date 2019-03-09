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


		headers = {
			"Content-type" : content_type
		}


		fh = open(filepath, mode)
		file_contents = fh.read()

		if mode == "rb":
			content = file_contents
		else:
			content = bytes(file_contents, "UTF-8")


		super().__init__(200, headers, content)
