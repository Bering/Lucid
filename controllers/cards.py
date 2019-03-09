import response
from controllers.base import Controller

class CardsController(Controller):
	def __init__(self):
		pass

	def do_GET(self, parts):
		username = parts[0]
		project_name = parts[1]
		card_id = parts[2]
		return response.Response404NotFound()
		