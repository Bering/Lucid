import response
from controllers.base import Controller

class ConfigController(Controller):
	def __init__(self):
		pass

	def do_GET(self, parts):
		return response.Response404NotFound()
