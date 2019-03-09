class Response:

	def __init__(self, status, headers, content):
		self.status = status
		self.headers = headers
		self.content = content
