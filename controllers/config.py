import response
from controllers.base import Controller

class ConfigController(Controller):
	def __init__(self, form_fields):
		super().__init__(form_fields)

	def do_GET(self, parts):
		return response.Response404NotFound()
