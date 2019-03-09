from response import Response

class Response404NotFound(Response):

	def __init__(self, filepath):
		super().__init__(404, "text/plain", "404 Not Found")
