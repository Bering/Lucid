import os
from response import Response

class ResponseFile(Response):

	def __init__(self, filepath):

		# TODO: Check date and return 304 Not Modified?

		f = open(filepath, "r")
		content = f.read()
		super().__init__(200, "text/html", content)
