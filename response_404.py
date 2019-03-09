from response import Response

class Response404NotFound(Response):

	def __init__(self):
		super().__init__(
			404,
			{ "Content-type" : "text/plain" },
			bytes("404 Not Found", "UTF-8")
		)
